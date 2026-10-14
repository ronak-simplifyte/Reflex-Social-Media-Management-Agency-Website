import reflex as rx

import json
import logging
import re
from typing import Any
from sqlalchemy import text

from app.content import PLATFORMS, SERVICE_CATEGORIES


class CustomPlanState(rx.State):
    busy: bool = False
    message: str = ""
    saved: bool = False

    @rx.event
    def begin_enquiry(self):
        self.message = ""
        self.saved = False

    @rx.event
    async def submit_enquiry(self, form_data: dict[str, Any]):
        if self.busy or self.saved:
            return
        self.message = ""
        values = {
            key: str(form_data.get(key, "")).strip()
            for key in (
                "name",
                "business_name",
                "phone",
                "whatsapp",
                "email",
                "industry",
                "message",
                "posts",
                "reels",
                "budget",
            )
        }
        if any(
            not values[key]
            for key in (
                "name",
                "business_name",
                "phone",
                "whatsapp",
                "email",
                "industry",
                "message",
            )
        ):
            self.message = (
                "Please complete all required business and contact details."
            )
            return
        limits = {
            "name": 200,
            "business_name": 250,
            "phone": 32,
            "whatsapp": 32,
            "email": 320,
            "industry": 200,
            "message": 5000,
        }
        if any(len(values[key]) > limit for key, limit in limits.items()):
            self.message = (
                "One or more fields are too long. Please shorten your details."
            )
            return
        if not re.fullmatch(
            r"[^\s@]+@[^\s@]+\.[^\s@]+", values["email"]
        ) or any(
            not re.fullmatch(r"\+?[0-9 ()-]{7,32}", values[key])
            or not 7 <= len(re.sub(r"\D", "", values[key])) <= 15
            for key in ("phone", "whatsapp")
        ):
            self.message = "Please enter a valid email and phone / WhatsApp numbers (7–15 digits)."
            return
        platforms = [
            item["id"]
            for item in PLATFORMS
            if form_data.get(f"platform_{item['id']}")
        ]
        services = [
            service["id"]
            for category in SERVICE_CATEGORIES
            for service in category["services"]
            if form_data.get(f"service_{service['id']}")
        ]
        requirements = {
            key: str(form_data.get(key, "")).strip()
            for key in (
                "advertising",
                "photography",
                "videography",
                "community",
            )
        }
        if not platforms or not services:
            self.message = "Choose at least one required platform and service."
            return
        if any(
            value not in ("Required", "Not required", "Discuss with me")
            for value in requirements.values()
        ):
            self.message = "Please specify your advertising, production and community requirements."
            return
        try:
            posts, reels = int(values["posts"]), int(values["reels"])
            budget_paise = int(values["budget"]) * 100
            if (
                not 0 <= posts <= 1000
                or not 0 <= reels <= 1000
                or not 0 < budget_paise <= 1000000000
            ):
                raise ValueError("Out of range")
        except ValueError:
            self.message = "Enter whole-number posts and reels (0–1,000) and a monthly budget from ₹1 to ₹1,00,00,000."
            return
        self.busy = True
        yield
        try:
            async with rx.asession() as session:
                result = await session.execute(
                    text("""
                    INSERT INTO custom_plan_enquiry
                    (name, business_name, email, phone, whatsapp, industry, platforms, services,
                     social_profile_urls, requirements, posts_per_month, reels_per_month,
                     budget_min_paise, budget_max_paise, message)
                    VALUES (:name, :business_name, :email, :phone, :whatsapp, :industry,
                     CAST(:platforms AS JSON), CAST(:services AS JSON), CAST(:profiles AS JSON),
                     :requirements, :posts, :reels, :budget, :budget, :message)
                    RETURNING id
                """),
                    {
                        **{key: values[key] for key in limits},
                        "platforms": json.dumps(platforms),
                        "services": json.dumps(services),
                        "profiles": "[]",
                        "requirements": json.dumps(requirements),
                        "posts": posts,
                        "reels": reels,
                        "budget": budget_paise,
                    },
                )
                reference = int(result.scalar_one())
                await session.commit()
            self.saved = True
            self.message = f"Your custom-plan enquiry has been saved. Reference CP-{reference}. This is a request for a quotation, not an order or payment."
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.message = "We couldn’t save your enquiry. Your entries are still here — please try again."
        finally:
            self.busy = False
