import reflex as rx

import hashlib
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Any
from sqlalchemy import text


class ContactState(rx.State):
    busy: bool = False
    saved: bool = False
    feedback: str = ""
    errors: dict[str, str] = {
        "name": "",
        "phone": "",
        "email": "",
        "business_name": "",
        "subject": "",
        "message": "",
    }
    form_version: int = 0
    _last_fingerprint: str = ""
    _last_saved_at: float = 0.0

    def _validate(self, values: dict[str, str]) -> dict[str, str]:
        labels = {
            "name": "Name",
            "phone": "Phone",
            "email": "Email",
            "business_name": "Business Name",
            "subject": "Subject",
            "message": "Message",
        }
        limits = {
            "name": 200,
            "phone": 32,
            "email": 320,
            "business_name": 250,
            "subject": 250,
            "message": 5000,
        }
        errors = {key: "" for key in labels}
        for key, label in labels.items():
            if not values[key]:
                errors[key] = f"Enter your {label.lower()}."
            elif len(values[key]) > limits[key]:
                errors[key] = (
                    f"Keep {label.lower()} within {limits[key]} characters."
                )
            elif any(
                ord(char) < 32 and char not in "\n\r\t" for char in values[key]
            ):
                errors[key] = (
                    f"Remove unsupported characters from {label.lower()}."
                )
        if values["email"] and not re.fullmatch(
            r"[^\s@]+@[^\s@]+\.[^\s@]+", values["email"]
        ):
            errors["email"] = "Enter a valid email address."
        phone = values["phone"]
        if phone and (
            not re.fullmatch(r"\+?[0-9 ()-]{7,32}", phone)
            or not 7 <= len(re.sub(r"\D", "", phone)) <= 15
        ):
            errors["phone"] = (
                "Enter a phone number with 7–15 digits; include your country code where applicable."
            )
        return errors

    @rx.event
    def clear_form(self):
        if self.busy:
            return
        self.form_version += 1
        self.saved = False
        self.feedback = "Form cleared. You can start a new enquiry."
        self.errors = {key: "" for key in self.errors}

    @rx.event
    async def submit_contact(self, form_data: dict[str, Any]):
        if self.busy or self.saved:
            return
        values = {
            key: str(form_data.get(key, "")).strip() for key in self.errors
        }
        self.errors = self._validate(values)
        if any(self.errors.values()):
            self.feedback = "Your enquiry has not been sent. Please correct the marked fields below."
            yield rx.set_focus("contact-feedback")
            return
        fingerprint = hashlib.sha256(
            repr(tuple(values.items())).encode()
        ).hexdigest()
        now = datetime.now(timezone.utc)
        if (
            fingerprint == self._last_fingerprint
            and now.timestamp() - self._last_saved_at < 300
        ):
            self.feedback = "This enquiry was already saved. Please allow time for it to be reviewed; no duplicate was sent."
            yield rx.set_focus("contact-feedback")
            return
        self.busy = True
        self.feedback = "Saving your enquiry…"
        yield
        try:
            async with rx.asession() as session:
                await session.execute(
                    text("LOCK TABLE lead IN SHARE ROW EXCLUSIVE MODE")
                )
                await session.execute(
                    text("""
                        INSERT INTO lead (name, phone, email, business_name, subject, message)
                        SELECT :name, :phone, :email, :business_name, :subject, :message
                        WHERE NOT EXISTS (
                            SELECT 1 FROM lead
                            WHERE name = :name AND phone = :phone AND email = :email
                              AND business_name = :business_name AND subject = :subject
                              AND message = :message AND created_at >= :since
                        )
                    """),
                    {**values, "since": now - timedelta(minutes=5)},
                )
                await session.commit()
            self._last_fingerprint = fingerprint
            self._last_saved_at = now.timestamp()
            self.saved = True
            self.form_version += 1
            self.feedback = "Your enquiry has been saved. Thank you for sharing your needs. This is not an order; the business identity and response availability are still pending verification. No response time is guaranteed."
        except Exception as e:
            logging.exception(
                f"Error: {type(e).__name__} while saving contact enquiry"
            )
            self.feedback = "We couldn’t save your enquiry. Your entries are still here. Please try again later; nothing has been confirmed."
        finally:
            self.busy = False
        yield rx.set_focus("contact-feedback")
