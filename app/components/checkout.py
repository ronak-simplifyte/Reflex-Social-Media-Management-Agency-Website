import reflex as rx

from app.components.navigation import navigation
from app.components.home_sections import footer
from app.components.contact import floating_contact
from app.components.plan_forms import CONTACT_FIELDS, contact_field
from app.content import PRICING
from app.states.home_state import HomeState
from app.states.checkout_state import CheckoutState


def payment_outcome() -> rx.Component:
    return rx.el.div(
        rx.match(
            CheckoutState.view,
            (
                "paid",
                rx.icon(
                    "circle-check",
                    class_name="mb-6 h-10 w-10 text-[var(--ink)]",
                ),
            ),
            (
                "cancelled",
                rx.icon(
                    "circle-pause",
                    class_name="mb-6 h-10 w-10 text-[var(--display)]",
                ),
            ),
            rx.icon(
                "circle-alert",
                class_name="mb-6 h-10 w-10 text-[var(--display)]",
            ),
        ),
        rx.el.h2(
            rx.match(
                CheckoutState.view,
                ("paid", "A considered next step."),
                ("cancelled", "Take your time."),
                ("unconfirmed", "Let’s check before you retry."),
                "A little pause, not the end.",
            ),
            class_name="font-['Playfair_Display'] text-3xl text-[var(--ink)]",
        ),
        rx.el.p(
            CheckoutState.feedback,
            role="status",
            aria_live="polite",
            class_name="mt-5 text-sm leading-7 text-[var(--muted)]",
        ),
        rx.cond(
            CheckoutState.view == "paid",
            rx.el.div(
                rx.el.p(
                    f"Thank you, {CheckoutState.paid_name}.",
                    class_name="text-sm font-semibold text-[var(--ink)]",
                ),
                rx.el.p(
                    f"{CheckoutState.paid_plan} · {CheckoutState.paid_duration}",
                    class_name="mt-4 text-sm text-[var(--ink)]",
                ),
                rx.el.p(
                    CheckoutState.paid_amount,
                    class_name="mt-3 text-3xl font-semibold text-[var(--ink)]",
                ),
                rx.el.p(
                    "PAYMENT REFERENCE",
                    class_name="mt-6 text-[10px] font-semibold tracking-wider text-[var(--muted)]",
                ),
                rx.el.p(
                    CheckoutState.reference,
                    class_name="mt-2 break-all text-sm text-[var(--ink)]",
                ),
                class_name="mt-6 rounded-xl border border-[var(--line)] bg-[var(--surface)] p-5",
            ),
            rx.cond(
                CheckoutState.view == "unconfirmed",
                rx.el.button(
                    rx.cond(
                        CheckoutState.busy,
                        "Checking payment…",
                        "Check payment again",
                    ),
                    type="button",
                    on_click=CheckoutState.verify_payment,
                    disabled=CheckoutState.busy,
                    class_name="mt-6 min-h-12 w-full rounded-full bg-[var(--primary)] px-6 py-3 text-sm font-semibold text-[var(--on-primary)] disabled:opacity-60",
                ),
                rx.el.button(
                    "Review details & retry",
                    type="button",
                    on_click=CheckoutState.edit_details,
                    disabled=CheckoutState.busy,
                    class_name="mt-6 min-h-12 w-full rounded-full bg-[var(--primary)] px-6 py-3 text-sm font-semibold text-[var(--on-primary)] disabled:opacity-60",
                ),
            ),
        ),
        class_name="rounded-2xl border border-[var(--line)] bg-[var(--paper)] p-6 sm:p-8",
    )


def checkout_form() -> rx.Component:
    return rx.el.form(
        rx.el.h2(
            "Your details", class_name="text-xl font-semibold text-[var(--ink)]"
        ),
        rx.el.p(
            "All fields are required. Phone and WhatsApp: 7–15 digits, including country code where applicable. Never share card details or passwords here.",
            class_name="mt-3 text-xs leading-6 text-[var(--muted)]",
        ),
        rx.el.fieldset(
            rx.el.div(
                rx.foreach(
                    CONTACT_FIELDS,
                    lambda field: contact_field(
                        field, "checkout", CheckoutState.customer[field[0]]
                    ),
                ),
                class_name="grid grid-cols-1 gap-5 sm:grid-cols-2",
            ),
            disabled=CheckoutState.busy | (CheckoutState.view == "pending"),
            class_name="mt-7",
        ),
        rx.el.p(
            CheckoutState.feedback,
            role="status",
            aria_live="polite",
            class_name="mt-5 text-sm leading-7 text-[var(--ink)]",
        ),
        rx.el.button(
            rx.cond(
                CheckoutState.busy,
                "Preparing checkout…",
                f"Pay {CheckoutState.total_label}",
            ),
            type="submit",
            disabled=CheckoutState.busy
            | (CheckoutState.view == "pending")
            | (CheckoutState.checkout_notice != ""),
            class_name="mt-6 flex min-h-12 w-full items-center justify-center gap-3 rounded-full bg-[#D7BE82] px-6 py-3 text-sm font-semibold text-[#0C2A20] disabled:cursor-not-allowed disabled:opacity-60",
        ),
        rx.el.p(
            "Secure Standard Checkout by Razorpay. No card information is stored by this website. Payment is accepted only after server verification of captured funds.",
            class_name="mt-4 text-xs leading-6 text-[var(--muted)]",
        ),
        on_submit=CheckoutState.start_payment,
        reset_on_submit=False,
        class_name="rounded-2xl border border-[var(--line)] bg-[var(--paper)] p-6 sm:p-8",
    )


def checkout_page() -> rx.Component:
    return rx.el.div(
        navigation(),
        rx.el.main(
            rx.el.a(
                rx.icon("arrow-left", class_name="h-4 w-4"),
                "Back to plans",
                href="/#plans",
                class_name="mb-5 inline-flex min-h-11 items-center gap-2 text-sm text-[var(--ink)]",
            ),
            rx.el.p(
                "THE SOCIAL ATELIER · CHECKOUT",
                class_name="text-[10px] font-semibold tracking-[0.18em] text-[var(--muted)]",
            ),
            rx.el.h1(
                "Your next chapter, ",
                rx.el.em(
                    "thoughtfully scoped.",
                    class_name="font-['Playfair_Display'] font-normal",
                ),
                class_name="mt-5 text-3xl font-medium tracking-tight text-[var(--ink)] sm:text-4xl",
            ),
            rx.cond(
                CheckoutState.checkout_notice != "",
                rx.el.div(
                    rx.icon(
                        "info",
                        class_name="mt-1 h-5 w-5 shrink-0 text-[var(--ink)]",
                    ),
                    rx.el.p(
                        CheckoutState.checkout_notice,
                        class_name="text-sm leading-7 text-[var(--ink)]",
                    ),
                    role="status",
                    class_name="mt-7 flex gap-3 rounded-xl border border-[var(--line)] bg-[var(--surface)] p-5",
                ),
            ),
            rx.el.div(
                rx.el.aside(
                    rx.el.p(
                        "YOUR SELECTED SCOPE",
                        class_name="text-[10px] font-semibold tracking-wider text-[#D7BE82]",
                    ),
                    rx.el.h2(
                        CheckoutState.plan_name,
                        class_name="mt-6 text-2xl font-semibold text-[#F7F2E7]",
                    ),
                    rx.el.p(
                        CheckoutState.duration_label,
                        class_name="mt-3 text-sm text-[#D8D0BD]",
                    ),
                    rx.el.p(
                        CheckoutState.total_label,
                        class_name="mt-7 text-4xl font-semibold tracking-tight text-[#F7F2E7]",
                    ),
                    rx.el.p(
                        "Exact service total for the full duration. Not a monthly instalment.",
                        class_name="mt-3 text-xs leading-6 text-[#D8D0BD]",
                    ),
                    rx.el.p(
                        PRICING["tax_notice"],
                        class_name="mt-6 border-t border-[#355547] pt-6 text-xs leading-6 text-[#D8D0BD]",
                    ),
                    rx.el.p(
                        "Ad spend, creator fees, shoots, travel and third-party licences are excluded. Final scope and commercial terms must be agreed before payment is enabled.",
                        class_name="mt-4 text-xs leading-6 text-[#D8D0BD]",
                    ),
                    class_name="h-fit min-w-0 rounded-t-[48px] rounded-b-xl bg-[#153B2B] p-6 sm:p-8",
                ),
                rx.match(
                    CheckoutState.view,
                    ("details", checkout_form()),
                    ("pending", checkout_form()),
                    payment_outcome(),
                ),
                class_name="mt-8 grid w-full grid-cols-1 gap-6 md:grid-cols-[0.8fr_1.2fr]",
            ),
            id="main-content",
            tab_index=-1,
            class_name="mx-auto w-full min-w-0 max-w-5xl px-5 py-10 sm:px-8 sm:py-16",
        ),
        footer(),
        floating_contact(),
        custom_attrs={"data-theme": HomeState.theme},
        class_name="atelier min-h-dvh w-full min-w-0 overflow-x-clip bg-[var(--paper)] font-['Inter'] text-[var(--ink)]",
    )
