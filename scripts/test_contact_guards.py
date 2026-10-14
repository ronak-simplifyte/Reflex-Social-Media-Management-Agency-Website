import reflex as rx

import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from faker import Faker

from app.content import BUSINESS, WHATSAPP_VERIFIED, verified_link
from app.states.contact_state import ContactState


class ContactGuards(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        fake = Faker()
        self.values = {
            "name": fake.name(),
            "business_name": fake.company(),
            "email": fake.email(),
            "phone": "+919876543210",
            "subject": "Social media enquiry",
            "message": fake.paragraph(),
        }

    async def submit(self, state, values):
        async for _ in state.submit_contact(values):
            pass

    def test_placeholders_are_never_verified(self):
        self.assertFalse(WHATSAPP_VERIFIED)
        for group in ("contact_links", "social_links"):
            for link in BUSINESS[group].values():
                self.assertTrue(link["value"])
                self.assertFalse(verified_link(link))
                self.assertFalse(
                    verified_link(
                        {**link, "enabled": True, "is_placeholder": False}
                    )
                )

    def test_validation_and_limits(self):
        state = ContactState()
        self.assertFalse(any(state._validate(self.values).values()))
        invalid = {
            **self.values,
            "email": "invalid",
            "phone": "123",
            "message": "x" * 5001,
        }
        errors = state._validate(invalid)
        self.assertTrue(errors["email"])
        self.assertTrue(errors["phone"])
        self.assertTrue(errors["message"])

    async def test_invalid_never_touches_database(self):
        state = ContactState()
        with patch.object(rx, "asession") as database:
            await self.submit(state, {**self.values, "name": " "})
            database.assert_not_called()
        self.assertFalse(state.saved)
        self.assertEqual(state.form_version, 0)

    async def test_save_is_parameterized_and_duplicate_is_blocked(self):
        state = ContactState()
        session = MagicMock()
        session.execute = AsyncMock()
        session.commit = AsyncMock()
        manager = MagicMock()
        manager.__aenter__ = AsyncMock(return_value=session)
        manager.__aexit__ = AsyncMock(return_value=False)
        values = {**self.values, "subject": "O'Reilly; DROP TABLE lead;"}
        with patch.object(rx, "asession", return_value=manager):
            await self.submit(state, values)
            self.assertTrue(state.saved)
            self.assertEqual(state.form_version, 1)
            statement, parameters = session.execute.call_args.args
            self.assertIn("INSERT INTO lead", str(statement))
            self.assertNotIn(values["subject"], str(statement))
            self.assertEqual(parameters["subject"], values["subject"])
            session.commit.assert_awaited_once()
            await self.submit(state, values)
            self.assertEqual(session.execute.await_count, 2)
            state.clear_form()
            await self.submit(state, values)
            self.assertEqual(session.execute.await_count, 2)

    async def test_error_preserves_form_and_redacts_feedback(self):
        state = ContactState()
        with (
            patch.object(
                rx,
                "asession",
                side_effect=RuntimeError("private database details"),
            ),
            patch("logging.exception"),
        ):
            await self.submit(state, self.values)
        self.assertFalse(state.saved)
        self.assertFalse(state.busy)
        self.assertEqual(state.form_version, 0)
        self.assertNotIn("private database", state.feedback)
        self.assertIn("entries are still here", state.feedback)

    async def test_busy_does_not_submit(self):
        state = ContactState()
        state.busy = True
        with patch.object(rx, "asession") as database:
            await self.submit(state, self.values)
            database.assert_not_called()


if __name__ == "__main__":
    unittest.main()
