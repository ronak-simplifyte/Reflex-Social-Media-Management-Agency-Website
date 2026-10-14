import reflex as rx

import unittest
from unittest.mock import patch

from app.content import PRICING
from app.states.checkout_state import CheckoutState
from app.states.pricing_state import PricingState


class CheckoutGuards(unittest.IsolatedAsyncioTestCase):
    def test_explicit_monthly_prices_and_preserved_totals(self):
        self.assertEqual(
            [
                plan["prices"]["monthly"]["total_inr"]
                for plan in PRICING["plans"]
            ],
            [9999, 19999, 34999],
        )
        self.assertEqual(
            [
                plan["prices"]["six_months"]["total_inr"]
                for plan in PRICING["plans"]
            ],
            [51000, 84000, 138000],
        )
        self.assertFalse(PRICING["approved_for_checkout"])

    def test_trusted_selection_and_paise(self):
        state = CheckoutState()
        state.plan_id = "premium"
        state.duration_id = "one_year"
        self.assertEqual(state._selection(), ("Premium", 12, 25200000))
        state.plan_id = "arbitrary-client-plan"
        with self.assertRaises(ValueError):
            state._selection()

    def test_savings_math(self):
        state = PricingState()
        state.duration = "six_months"
        self.assertEqual(
            [card["savings"] for card in state.cards],
            [
                "Save ₹8,994 versus 6 Monthly periods",
                "Save ₹35,994 versus 6 Monthly periods",
                "Save ₹71,994 versus 6 Monthly periods",
            ],
        )

    async def test_commercial_hold_never_calls_provider_or_database(self):
        state = CheckoutState()
        with (
            patch("app.states.checkout_state.razorpay.Client") as client,
            patch.object(rx, "asession") as database,
        ):
            async for _ in state.start_payment(
                {
                    "name": "Validation User",
                    "business_name": "Validation Business",
                    "phone": "+919876543210",
                    "whatsapp": "+919876543210",
                    "email": "validation@example.com",
                }
            ):
                pass
            client.assert_not_called()
            database.assert_not_called()
            self.assertIn("on hold", state.feedback)
            self.assertFalse(state.busy)

    async def test_missing_configuration_never_creates_pending_order(self):
        state = CheckoutState()
        state.busy = True
        with (
            patch.dict(PRICING, {"approved_for_checkout": True}),
            patch.dict(
                "os.environ", {"RAZORPAY_KEY_ID": "", "RAZORPAY_KEY_SECRET": ""}
            ),
            patch("app.states.checkout_state.razorpay.Client") as client,
            patch.object(rx, "asession") as database,
            patch("logging.exception"),
        ):
            async for _ in state.create_order():
                pass
            client.assert_not_called()
            database.assert_not_called()
            self.assertEqual(state.view, "failed")
            self.assertEqual(state._owned_orders, {})


if __name__ == "__main__":
    unittest.main()
