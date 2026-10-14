import reflex as rx

from typing import TypedDict

from app.content import PRICING, DurationId


class PricingCard(TypedDict):
    id: str
    name: str
    description: str
    highlighted: bool
    features: list[str]
    total_inr: int
    savings: str


class PricingState(rx.State):
    duration: str = PRICING["default_duration_id"]

    @rx.event
    def select_duration(self, duration: str):
        if duration in {item["id"] for item in PRICING["durations"]}:
            self.duration = duration

    @rx.var
    def duration_label(self) -> str:
        return next(
            item["label"]
            for item in PRICING["durations"]
            if item["id"] == self.duration
        )

    @rx.var
    def cards(self) -> list[PricingCard]:
        duration: DurationId = next(
            item["id"]
            for item in PRICING["durations"]
            if item["id"] == self.duration
        )
        months = next(
            item["months"]
            for item in PRICING["durations"]
            if item["id"] == duration
        )
        cards: list[PricingCard] = []
        for plan in PRICING["plans"]:
            price = plan["prices"][duration]
            saving = (
                plan["prices"]["monthly"]["total_inr"] * months
                - price["total_inr"]
            )
            cards.append(
                {
                    "id": plan["id"],
                    "name": plan["name"],
                    "description": plan["description"],
                    "highlighted": plan["highlighted"],
                    "features": plan["features"],
                    "total_inr": price["total_inr"],
                    "savings": f"Save ₹{saving:,} versus {months} Monthly periods"
                    if price["savings_label"] and months > 1 and saving > 0
                    else "",
                }
            )
        return cards
