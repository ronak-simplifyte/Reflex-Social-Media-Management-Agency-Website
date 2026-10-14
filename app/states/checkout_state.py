import reflex as rx

import asyncio
import hashlib
import hmac
import json
import logging
import os
import re
import uuid
from typing import Any

import razorpay
from sqlalchemy import text
from app.content import PRICING


class CheckoutState(rx.State):
    plan_id: str = "standard"
    duration_id: str = "monthly"
    customer: dict[str, str] = {
        "name": "",
        "business_name": "",
        "phone": "",
        "whatsapp": "",
        "email": "",
    }
    busy: bool = False
    view: str = "details"
    feedback: str = ""
    reference: str = ""
    paid_name: str = ""
    paid_plan: str = ""
    paid_duration: str = ""
    paid_amount: str = ""
    _owned_orders: dict[str, int] = {}
    _active_order: str = ""
    _last_success: dict[str, str] = {}

    def _selection(self) -> tuple[str, int, int]:
        plan = next(
            (plan for plan in PRICING["plans"] if plan["id"] == self.plan_id),
            None,
        )
        duration = next(
            (
                duration
                for duration in PRICING["durations"]
                if duration["id"] == self.duration_id
            ),
            None,
        )
        if plan is None or duration is None:
            raise ValueError("Invalid plan or duration")
        total = plan["prices"][duration["id"]]["total_inr"]
        if type(total) is not int or total <= 0 or PRICING["currency"] != "INR":
            raise ValueError("Invalid commercial pricing")
        return plan["name"], duration["months"], total * 100

    @rx.var
    def plan_name(self) -> str:
        return self._selection()[0]

    @rx.var
    def duration_label(self) -> str:
        return next(
            item["label"]
            for item in PRICING["durations"]
            if item["id"] == self.duration_id
        )

    @rx.var
    def total_label(self) -> str:
        return f"₹{self._selection()[2] // 100:,}"

    @rx.var
    def checkout_notice(self) -> str:
        notices: list[str] = []
        if not PRICING["approved_for_checkout"]:
            notices.append(
                "Sample pricing only. Payments are on hold until the business owner confirms commercial terms, taxes and business details."
            )
        if not os.getenv("RAZORPAY_KEY_ID") or not os.getenv(
            "RAZORPAY_KEY_SECRET"
        ):
            notices.append(
                "Payment configuration is unavailable. No payment can be taken."
            )
        return " ".join(notices)

    @rx.event
    def load_checkout(self):
        query = self.router.url.query_parameters
        plan = str(query.get("plan", "standard"))
        duration = str(query.get("duration", "monthly"))
        if plan not in {
            item["id"] for item in PRICING["plans"]
        } or duration not in {item["id"] for item in PRICING["durations"]}:
            self.feedback = (
                "That selection is unavailable. Please choose a listed plan."
            )
            return
        if self.view != "paid" and not self.busy and self.view != "pending":
            self.plan_id, self.duration_id = plan, duration

    @rx.event
    async def start_payment(self, form_data: dict[str, Any]):
        if self.busy or self.view in ("pending", "paid"):
            return
        self.customer = {
            key: str(form_data.get(key, "")).strip() for key in self.customer
        }
        limits = {
            "name": 200,
            "business_name": 250,
            "phone": 32,
            "whatsapp": 32,
            "email": 320,
        }
        if any(
            not self.customer[key] or len(self.customer[key]) > limit
            for key, limit in limits.items()
        ):
            self.feedback = "Please complete all contact details within the indicated field limits."
            return
        if not re.fullmatch(
            r"[^\s@]+@[^\s@]+\.[^\s@]+", self.customer["email"]
        ) or any(
            not re.fullmatch(r"\+?[0-9 ()-]{7,32}", self.customer[key])
            or not 7 <= len(re.sub(r"\D", "", self.customer[key])) <= 15
            for key in ("phone", "whatsapp")
        ):
            self.feedback = "Enter a valid email and phone / WhatsApp numbers (7–15 digits)."
            return
        if self.checkout_notice:
            self.feedback = self.checkout_notice
            return
        self.busy = True
        self.feedback = "Preparing secure checkout…"
        yield CheckoutState.create_order

    @rx.event
    async def create_order(self):
        if not self.busy or self.view == "paid":
            return
        try:
            if not PRICING["approved_for_checkout"]:
                raise ValueError("Commercial approval required")
            key_id, secret = (
                os.getenv("RAZORPAY_KEY_ID", ""),
                os.getenv("RAZORPAY_KEY_SECRET", ""),
            )
            if not key_id or not secret:
                raise ValueError("Payment configuration unavailable")
            plan_name, months, amount = self._selection()
            client = razorpay.Client(auth=(key_id, secret))
            provider = await asyncio.to_thread(
                client.order.create,
                data={
                    "amount": amount,
                    "currency": "INR",
                    "receipt": f"sa_{uuid.uuid4().hex}",
                    "partial_payment": False,
                },
            )
            provider_id = str(provider.get("id", ""))
            if (
                not provider_id.startswith("order_")
                or provider.get("amount") != amount
                or provider.get("currency") != "INR"
            ):
                raise ValueError("Provider order mismatch")
            async with rx.asession() as session:
                result = await session.execute(
                    text("""
                    INSERT INTO "order" (customer_name, business_name, phone, whatsapp, email,
                        plan_id, plan_name, duration_months, amount_paise, currency, status, provider_order_id)
                    VALUES (:name, :business_name, :phone, :whatsapp, :email, :plan_id, :plan_name,
                        :months, :amount, 'INR', 'pending', :provider_id) RETURNING id
                """),
                    {
                        **self.customer,
                        "plan_id": self.plan_id,
                        "plan_name": plan_name,
                        "months": months,
                        "amount": amount,
                        "provider_id": provider_id,
                    },
                )
                local_id = int(result.scalar_one())
                await session.execute(
                    text(
                        "INSERT INTO payment_attempt (order_id, provider_order_id, status) VALUES (:id, :provider_id, 'pending')"
                    ),
                    {"id": local_id, "provider_id": provider_id},
                )
                await session.commit()
            self._owned_orders[provider_id] = local_id
            self._active_order = provider_id
            self.view = "pending"
            self.feedback = "Complete the secure payment window. Payment is confirmed only after server verification."
            metadata = json.dumps(
                {
                    "key": key_id,
                    "order_id": provider_id,
                    "amount": amount,
                    "currency": "INR",
                    "description": f"{plan_name} · {months} month(s)",
                }
            )
            script = """new Promise((resolve) => {
                const options = OPTIONS;
                let done = false;
                const finish = (payload) => { if (!done) { done = true; resolve(JSON.stringify(payload)); } };
                const open = () => {
                    try {
                        const checkout = new window.Razorpay({...options,
                            retry: {enabled: false},
                            handler: (r) => finish({kind: 'success', order: options.order_id,
                                callback_order: r.razorpay_order_id, payment: r.razorpay_payment_id, signature: r.razorpay_signature}),
                            modal: {ondismiss: () => finish({kind: 'cancelled', order: options.order_id})}
                        });
                        checkout.on('payment.failed', () => { finish({kind: 'failed', order: options.order_id}); checkout.close(); });
                        checkout.open();
                    } catch (_) { finish({kind: 'failed', order: options.order_id}); }
                };
                if (window.Razorpay) { open(); } else {
                    const s = document.createElement('script'); s.src = 'https://checkout.razorpay.com/v1/checkout.js';
                    s.onload = open; s.onerror = () => finish({kind: 'failed', order: options.order_id});
                    document.head.appendChild(s);
                }
            })""".replace("OPTIONS", metadata)
            yield rx.call_script(script, callback=CheckoutState.record_payment)
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.view = "failed"
            self.feedback = "Secure checkout could not be started. No local pending order is created when the provider is unavailable. Please try again later."
        finally:
            self.busy = False

    @rx.event
    def record_payment(self, result: str):
        try:
            payload = json.loads(result)
            order = str(payload.get("order", ""))
            if order not in self._owned_orders:
                raise ValueError("Unknown checkout")
            kind = payload.get("kind")
            if kind == "success":
                self._last_success = {
                    key: str(payload.get(key, ""))
                    for key in (
                        "order",
                        "callback_order",
                        "payment",
                        "signature",
                    )
                }
                return CheckoutState.verify_payment
            if kind in ("failed", "cancelled"):
                return CheckoutState.handle_failed_payment(order, kind)
            raise ValueError("Invalid callback")
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.feedback = "The checkout response could not be processed. Payment has not been confirmed."

    @rx.event
    async def verify_payment(self):
        payload = dict(self._last_success)
        provider_id = payload.get("order", "")
        local_id = self._owned_orders.get(provider_id, 0)
        if not local_id or self.busy:
            return
        self.busy = True
        self.feedback = "Verifying your payment securely…"
        yield
        try:
            async with rx.asession() as session:
                row = (
                    (
                        await session.execute(
                            text(
                                'SELECT provider_order_id, amount_paise, currency FROM "order" WHERE id = :id'
                            ),
                            {"id": local_id},
                        )
                    )
                    .mappings()
                    .one()
                )
            secret = os.getenv("RAZORPAY_KEY_SECRET", "")
            key_id = os.getenv("RAZORPAY_KEY_ID", "")
            if not secret or not key_id:
                raise ValueError("Verification unavailable")
            server_order = str(row["provider_order_id"])
            expected = hmac.new(
                secret.encode(),
                f"{server_order}|{payload['payment']}".encode(),
                hashlib.sha256,
            ).hexdigest()
            if payload[
                "callback_order"
            ] != server_order or not hmac.compare_digest(
                expected, payload["signature"]
            ):
                raise ValueError("Invalid payment signature")
            client = razorpay.Client(auth=(key_id, secret))
            payment = await asyncio.to_thread(
                client.payment.fetch, payload["payment"]
            )
            if (
                payment.get("id") != payload["payment"]
                or payment.get("order_id") != server_order
                or payment.get("amount") != int(row["amount_paise"])
                or payment.get("currency") != row["currency"]
                or payment.get("status") != "captured"
            ):
                raise ValueError(
                    "Payment not confirmed captured with matching order and amount"
                )
            async with rx.asession() as session:
                locked = (
                    (
                        await session.execute(
                            text("""SELECT status, provider_payment_id, customer_name, plan_name, duration_months, amount_paise
                    FROM "order" WHERE id = :id FOR UPDATE"""),
                            {"id": local_id},
                        )
                    )
                    .mappings()
                    .one()
                )
                if (
                    locked["status"] == "paid"
                    and locked["provider_payment_id"] != payload["payment"]
                ):
                    raise ValueError("Already paid with another reference")
                if locked["status"] != "paid":
                    await session.execute(
                        text("""UPDATE "order" SET status = 'paid', provider_payment_id = :payment,
                        paid_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP WHERE id = :id"""),
                        {"id": local_id, "payment": payload["payment"]},
                    )
                    await session.execute(
                        text("""UPDATE payment_attempt SET status = 'paid', provider_payment_id = :payment,
                        completed_at = CURRENT_TIMESTAMP, verified_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP,
                        error_code = '', error_description = '' WHERE order_id = :id"""),
                        {"id": local_id, "payment": payload["payment"]},
                    )
                await session.commit()
            self.paid_name = str(locked["customer_name"])
            self.paid_plan = str(locked["plan_name"])
            months = int(locked["duration_months"])
            self.paid_duration = {
                1: "Monthly",
                6: "6 Months",
                12: "1 Year",
            }.get(months, f"{months} months")
            self.paid_amount = f"₹{int(locked['amount_paise']) / 100:,.2f}"
            self.reference = payload["payment"]
            self.view = "paid"
            self.feedback = "Payment captured and verified. Keep your reference for your records."
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.view = "unconfirmed"
            self.feedback = "We could not confirm a captured payment. If your account was debited, do not pay again yet. Use Check payment again to retry verification."
        finally:
            self.busy = False

    @rx.event
    async def handle_failed_payment(self, provider_id: str, status: str):
        local_id = self._owned_orders.get(provider_id, 0)
        if not local_id or status not in ("failed", "cancelled"):
            return
        try:
            async with rx.asession() as session:
                row = (
                    await session.execute(
                        text(
                            'SELECT status FROM "order" WHERE id = :id FOR UPDATE'
                        ),
                        {"id": local_id},
                    )
                ).one()
                if row[0] == "paid":
                    return
                await session.execute(
                    text("""UPDATE "order" SET status = :status, updated_at = CURRENT_TIMESTAMP,
                    failed_at = CASE WHEN :status = 'failed' THEN CURRENT_TIMESTAMP ELSE failed_at END,
                    cancelled_at = CASE WHEN :status = 'cancelled' THEN CURRENT_TIMESTAMP ELSE cancelled_at END
                    WHERE id = :id"""),
                    {"id": local_id, "status": status},
                )
                await session.execute(
                    text("""UPDATE payment_attempt SET status = :status, error_code = :status,
                    error_description = :description, completed_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP
                    WHERE order_id = :id AND status != 'paid' """),
                    {
                        "id": local_id,
                        "status": status,
                        "description": "Customer dismissed checkout"
                        if status == "cancelled"
                        else "Checkout did not complete",
                    },
                )
                await session.commit()
            if provider_id == self._active_order and self.view != "paid":
                self.view = status
                self.feedback = (
                    "Checkout closed. No payment has been confirmed. Your details are retained."
                    if status == "cancelled"
                    else "Payment did not complete. Your details are retained; retry starts a new secure order."
                )
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.view = "unconfirmed"
            self.feedback = "We couldn’t record the checkout outcome. No payment has been confirmed. Please check your account before retrying."

    @rx.event
    def edit_details(self):
        if not self.busy and self.view not in ("pending", "paid"):
            self.view = "details"
            self.feedback = "Your details are retained. A new attempt creates a new payment order."
