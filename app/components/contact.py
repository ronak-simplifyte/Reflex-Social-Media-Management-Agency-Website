import reflex as rx

from app.content import (
    BUSINESS,
    PlaceholderLink,
    WHATSAPP_VERIFIED,
    verified_link,
)
from app.states.contact_state import ContactState


CONTACT_DETAILS: list[tuple[str, str, str, bool]] = [
    (link["label"], link["value"], link["url"], verified_link(link))
    for link in BUSINESS["contact_links"].values()
]
SOCIAL_DETAILS: list[tuple[str, str, str, bool]] = [
    (link["label"], link["value"], link["url"], verified_link(link))
    for link in BUSINESS["social_links"].values()
]
FIELDS: list[tuple[str, str, str, int, str]] = [
    ("name", "Name", "text", 200, "Your full name"),
    ("phone", "Phone", "tel", 32, "Your number, including country code"),
    ("email", "Email", "email", 320, "Your email address"),
    (
        "business_name",
        "Business Name",
        "text",
        250,
        "Your business or brand name",
    ),
    ("subject", "Subject", "text", 250, "What would you like to discuss?"),
]


def detail(label: str, value: str, url: str, enabled: bool) -> rx.Component:
    return rx.el.div(
        rx.el.p(label, class_name="text-xs font-semibold text-[var(--ink)]"),
        rx.cond(
            enabled,
            rx.el.a(
                value,
                rx.icon("arrow-up-right", class_name="h-4 w-4 shrink-0"),
                href=url,
                class_name="mt-2 flex min-h-11 items-center gap-2 break-words text-sm text-[var(--ink)] underline underline-offset-4",
            ),
            rx.el.div(
                rx.el.p(
                    value,
                    class_name="mt-2 break-words text-sm leading-6 text-[var(--muted)]",
                ),
                rx.el.p(
                    "Placeholder · not available until verified",
                    class_name="mt-1 text-xs leading-5 text-[var(--muted)]",
                ),
            ),
        ),
        key=label,
        class_name="min-w-0 border-b border-[var(--line)] py-5",
    )


def enquiry_field(field: tuple[str, str, str, int, str]) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            field[1],
            " *",
            html_for=f"contact-{field[0]}",
            class_name="block text-xs font-semibold text-[var(--ink)]",
        ),
        rx.el.input(
            id=f"contact-{field[0]}",
            name=field[0],
            type=field[2],
            required=True,
            max_length=field[3],
            placeholder=field[4],
            auto_complete=rx.match(
                field[0],
                ("name", "name"),
                ("email", "email"),
                ("phone", "tel"),
                ("business_name", "organization"),
                "off",
            ),
            aria_invalid=ContactState.errors[field[0]] != "",
            aria_describedby=f"contact-{field[0]}-error",
            class_name="mt-2 min-h-12 w-full min-w-0 rounded-lg border border-[var(--line)] bg-[var(--paper)] px-3 py-3 text-base text-[var(--ink)] placeholder:text-[var(--muted)] focus-visible:outline-2 focus-visible:outline-[#B79245]",
        ),
        rx.el.p(
            ContactState.errors[field[0]],
            id=f"contact-{field[0]}-error",
            class_name="mt-2 text-xs leading-5 text-[var(--ink)]",
        ),
        class_name="min-w-0",
    )


def contact_form() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Tell us what you have in mind.",
            class_name="text-xl font-semibold text-[var(--ink)]",
        ),
        rx.el.p(
            "All fields are required (*). Phone: 7–15 digits. This form stores an enquiry, not a booking. Do not send passwords, payment details or confidential information.",
            id="contact-instructions",
            class_name="mt-3 text-sm leading-7 text-[var(--muted)]",
        ),
        rx.el.p(
            ContactState.feedback,
            id="contact-feedback",
            tab_index=-1,
            role="status",
            aria_live="polite",
            aria_atomic=True,
            class_name="mt-5 text-sm font-medium leading-7 text-[var(--ink)]",
        ),
        rx.el.form(
            rx.el.fieldset(
                rx.el.legend("Your enquiry", class_name="sr-only"),
                rx.el.div(
                    rx.foreach(FIELDS, enquiry_field),
                    class_name="grid grid-cols-1 gap-4 sm:grid-cols-2",
                ),
                rx.el.label(
                    "Message *",
                    html_for="contact-message",
                    class_name="mt-5 block text-xs font-semibold text-[var(--ink)]",
                ),
                rx.el.textarea(
                    id="contact-message",
                    name="message",
                    required=True,
                    max_length=5000,
                    rows=5,
                    placeholder="Your goals, current challenges and the support you need (up to 5,000 characters).",
                    aria_invalid=ContactState.errors["message"] != "",
                    aria_describedby="contact-message-error",
                    class_name="mt-2 w-full min-w-0 resize-y rounded-lg border border-[var(--line)] bg-[var(--paper)] p-3 text-base text-[var(--ink)] placeholder:text-[var(--muted)] focus-visible:outline-2 focus-visible:outline-[#B79245]",
                ),
                rx.el.p(
                    ContactState.errors["message"],
                    id="contact-message-error",
                    class_name="mt-2 text-xs text-[var(--ink)]",
                ),
                disabled=ContactState.busy | ContactState.saved,
            ),
            rx.el.p(
                "By sending, you ask for your details to be used to review and respond to this enquiry. This does not subscribe you to marketing.",
                class_name="mt-5 text-xs leading-6 text-[var(--muted)]",
            ),
            rx.el.a(
                "Read the draft Privacy Policy",
                href="/privacy-policy",
                class_name="inline-flex min-h-11 items-center text-xs text-[var(--ink)] underline underline-offset-4",
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        ContactState.busy,
                        "Saving enquiry…",
                        rx.cond(
                            ContactState.saved, "Enquiry saved", "Send enquiry"
                        ),
                    ),
                    type="submit",
                    disabled=ContactState.busy | ContactState.saved,
                    class_name="flex min-h-12 items-center justify-center rounded-full bg-[var(--primary)] px-6 py-3 text-sm font-semibold text-[var(--on-primary)] disabled:cursor-not-allowed disabled:opacity-60",
                ),
                rx.el.button(
                    rx.cond(
                        ContactState.saved, "Start a new enquiry", "Clear form"
                    ),
                    type="button",
                    on_click=ContactState.clear_form,
                    disabled=ContactState.busy,
                    class_name="min-h-12 rounded-full border border-[var(--line)] bg-transparent px-6 py-3 text-sm text-[var(--ink)] hover:bg-[var(--surface)] disabled:opacity-60",
                ),
                class_name="mt-4 flex flex-col gap-3 sm:flex-row sm:flex-wrap",
            ),
            on_submit=ContactState.submit_contact,
            reset_on_submit=False,
            key=ContactState.form_version,
            aria_describedby="contact-instructions contact-feedback",
            aria_busy=ContactState.busy,
            class_name="mt-6",
        ),
        class_name="min-w-0 rounded-xl border border-[var(--line)] bg-[var(--surface)] p-5 sm:p-8",
    )


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.p(
            "10 / LET’S TALK",
            class_name="text-[10px] font-semibold tracking-[0.18em] text-[var(--muted)]",
        ),
        rx.el.h2(
            "A conversation before a commitment.",
            class_name="mt-5 font-['Playfair_Display'] text-3xl leading-tight text-[var(--ink)] sm:text-4xl",
        ),
        rx.el.p(
            "Share your needs using the form below. Enquiries can be saved now; the agency identity, direct contact channels and response availability are still awaiting owner verification.",
            class_name="mt-4 max-w-2xl text-sm leading-7 text-[var(--muted)]",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Contact details",
                    class_name="text-lg font-semibold text-[var(--ink)]",
                ),
                rx.foreach(
                    CONTACT_DETAILS,
                    lambda link: detail(
                        link[0],
                        link[1],
                        link[2],
                        link[3],
                    ),
                ),
                rx.el.p(
                    BUSINESS["address"],
                    class_name="mt-3 text-xs leading-6 text-[var(--muted)]",
                ),
                rx.el.h3(
                    "Find us on social",
                    class_name="mt-9 text-lg font-semibold text-[var(--ink)]",
                ),
                rx.el.div(
                    rx.foreach(
                        SOCIAL_DETAILS,
                        lambda link: detail(
                            link[0],
                            link[1],
                            link[2],
                            link[3],
                        ),
                    ),
                    class_name="grid grid-cols-1 gap-x-5 sm:grid-cols-2",
                ),
                class_name="min-w-0",
            ),
            contact_form(),
            class_name="mt-10 grid w-full grid-cols-1 items-start gap-10 lg:grid-cols-[0.85fr_1.15fr] lg:gap-14",
        ),
        id="contact",
        class_name="mx-auto w-full max-w-[1280px] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )


def floating_contact() -> rx.Component:
    return rx.cond(
        WHATSAPP_VERIFIED,
        rx.el.a(
            rx.icon("message-circle", class_name="h-5 w-5"),
            rx.el.span("WhatsApp", class_name="sr-only sm:not-sr-only"),
            href=BUSINESS["contact_links"]["whatsapp"]["url"],
            aria_label="Contact the verified business on WhatsApp",
            class_name="fixed bottom-4 right-4 z-30 flex min-h-12 items-center gap-2 rounded-full border border-[#355547] bg-[#153B2B] px-4 text-sm text-[#F7F2E7]",
        ),
        rx.el.a(
            rx.icon("mail", class_name="h-4 w-4"),
            rx.el.span("Enquire", class_name="sr-only sm:not-sr-only"),
            href="/#contact",
            aria_label="Go to contact enquiry form; WhatsApp is not yet verified",
            class_name="fixed bottom-4 right-4 z-30 flex min-h-11 items-center gap-2 rounded-full border border-[var(--line)] bg-[var(--paper)] px-3 text-xs text-[var(--ink)]",
        ),
    )
