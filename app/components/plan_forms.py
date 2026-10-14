import reflex as rx

from app.content import PLATFORMS, SERVICE_CATEGORIES
from app.states.custom_plan_state import CustomPlanState


CONTACT_FIELDS: list[tuple[str, str, str, int]] = [
    ("name", "Full Name", "text", 200),
    ("business_name", "Business Name", "text", 250),
    ("phone", "Phone", "tel", 32),
    ("whatsapp", "WhatsApp", "tel", 32),
    ("email", "Email", "email", 320),
]
REQUIREMENTS: list[tuple[str, str]] = [
    ("advertising", "Advertising"),
    ("photography", "Photography"),
    ("videography", "Videography"),
    ("community", "Community Management"),
]


def contact_field(
    field: tuple[str, str, str, int], prefix: str, default: str = ""
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            field[1],
            " *",
            html_for=f"{prefix}-{field[0]}",
            class_name="block text-xs font-semibold text-[var(--ink)]",
        ),
        rx.el.input(
            id=f"{prefix}-{field[0]}",
            name=field[0],
            type=field[2],
            required=True,
            max_length=field[3],
            default_value=default,
            key=default,
            auto_complete=rx.match(
                field[0],
                ("name", "name"),
                ("business_name", "organization"),
                ("email", "email"),
                "tel",
            ),
            class_name="mt-2 min-h-12 w-full min-w-0 rounded-lg border border-[var(--line)] bg-[var(--paper)] px-3 py-3 text-sm text-[var(--ink)] focus:border-[#B79245] focus:outline-2 focus:outline-[#B79245]",
        ),
        class_name="min-w-0",
    )


def number_field(
    name: str, label: str, maximum: int, minimum: int = 0
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            " *",
            html_for=f"custom-{name}",
            class_name="block text-xs font-semibold text-[var(--ink)]",
        ),
        rx.el.input(
            id=f"custom-{name}",
            name=name,
            type="number",
            min=minimum,
            max=maximum,
            step=1,
            required=True,
            placeholder="Whole numbers only",
            class_name="mt-2 min-h-12 w-full rounded-lg border border-[var(--line)] bg-[var(--paper)] px-3 text-sm text-[var(--ink)] focus:outline-2 focus:outline-[#B79245]",
        ),
        class_name="min-w-0",
    )


def requirement_select(item: tuple[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            item[1],
            " *",
            html_for=f"custom-{item[0]}",
            class_name="block text-xs font-semibold text-[var(--ink)]",
        ),
        rx.el.div(
            rx.el.select(
                rx.el.option("Choose an option", value=""),
                rx.el.option("Required", value="Required"),
                rx.el.option("Not required", value="Not required"),
                rx.el.option("Discuss with me", value="Discuss with me"),
                id=f"custom-{item[0]}",
                name=item[0],
                required=True,
                class_name="min-h-12 w-full appearance-none rounded-lg border border-[var(--line)] bg-[var(--paper)] px-3 pr-10 text-sm text-[var(--ink)] focus:outline-2 focus:outline-[#B79245]",
            ),
            rx.icon(
                "chevron-down",
                class_name="pointer-events-none absolute right-3 top-4 h-4 w-4 text-[var(--muted)]",
            ),
            class_name="relative mt-2",
        ),
        class_name="min-w-0",
    )


def custom_plan_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(
            rx.el.button(
                "Request a Custom Plan",
                rx.icon("arrow-up-right", class_name="h-4 w-4"),
                type="button",
                on_click=CustomPlanState.begin_enquiry,
                class_name="flex min-h-12 items-center justify-center gap-3 rounded-full border border-[var(--line)] bg-[var(--paper)] px-6 py-3 text-sm font-semibold text-[var(--ink)] hover:bg-[var(--surface)]",
            ),
            as_child=True,
        ),
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 z-50 bg-black/60"
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.radix.primitives.dialog.title(
                        "A scope that’s yours.",
                        class_name="text-2xl font-semibold tracking-tight text-[var(--ink)]",
                    ),
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            rx.icon("x", class_name="h-5 w-5"),
                            type="button",
                            aria_label="Close custom-plan form",
                            class_name="flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-[var(--line)] text-[var(--ink)]",
                        ),
                        as_child=True,
                    ),
                    class_name="flex items-start justify-between gap-4",
                ),
                rx.radix.primitives.dialog.description(
                    "Tell us about your business and the support you need. Required fields are marked *. This saves a quotation enquiry, not a purchase. The agency identity is still unverified; do not send passwords, card details or confidential information.",
                    class_name="mt-4 text-sm leading-7 text-[var(--muted)]",
                ),
                rx.el.form(
                    rx.el.fieldset(
                        rx.el.legend(
                            "01 / Your business",
                            class_name="mb-5 text-xs font-semibold uppercase tracking-wider text-[var(--ink)]",
                        ),
                        rx.el.div(
                            rx.foreach(
                                CONTACT_FIELDS,
                                lambda field: contact_field(field, "custom"),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Business Type *",
                                    html_for="custom-industry",
                                    class_name="block text-xs font-semibold text-[var(--ink)]",
                                ),
                                rx.el.input(
                                    id="custom-industry",
                                    name="industry",
                                    required=True,
                                    max_length=200,
                                    placeholder="e.g. café, retail, professional services",
                                    class_name="mt-2 min-h-12 w-full rounded-lg border border-[var(--line)] bg-[var(--paper)] px-3 text-sm text-[var(--ink)] focus:outline-2 focus:outline-[#B79245]",
                                ),
                            ),
                            class_name="grid grid-cols-1 gap-5 sm:grid-cols-2",
                        ),
                        disabled=CustomPlanState.busy | CustomPlanState.saved,
                    ),
                    rx.el.fieldset(
                        rx.el.legend(
                            "02 / Required Platforms *",
                            class_name="mb-4 text-xs font-semibold uppercase tracking-wider text-[var(--ink)]",
                        ),
                        rx.el.div(
                            rx.foreach(
                                PLATFORMS,
                                lambda platform: rx.el.label(
                                    rx.el.input(
                                        type="checkbox",
                                        name=f"platform_{platform['id']}",
                                        class_name="h-4 w-4 shrink-0 accent-[#B79245]",
                                    ),
                                    platform["name"],
                                    key=platform["id"],
                                    class_name="flex min-h-11 items-center gap-3 text-sm text-[var(--ink)]",
                                ),
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-2",
                        ),
                        disabled=CustomPlanState.busy | CustomPlanState.saved,
                        class_name="mt-8 border-t border-[var(--line)] pt-6",
                    ),
                    rx.el.fieldset(
                        rx.el.legend(
                            "03 / Required Services *",
                            class_name="mb-4 text-xs font-semibold uppercase tracking-wider text-[var(--ink)]",
                        ),
                        rx.foreach(
                            SERVICE_CATEGORIES,
                            lambda category: rx.el.details(
                                rx.el.summary(
                                    category["title"],
                                    rx.icon(
                                        "chevron-down",
                                        class_name="h-4 w-4 shrink-0",
                                    ),
                                    class_name="flex min-h-12 cursor-pointer items-center justify-between gap-3 text-sm font-medium text-[var(--ink)]",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        category["services"].to(
                                            list[dict[str, str]]
                                        ),
                                        lambda service: rx.el.label(
                                            rx.el.input(
                                                type="checkbox",
                                                name=f"service_{service['id']}",
                                                class_name="h-4 w-4 shrink-0 accent-[#B79245]",
                                            ),
                                            service["title"],
                                            key=service["id"],
                                            class_name="flex min-h-11 items-center gap-3 py-2 text-xs leading-5 text-[var(--ink)]",
                                        ),
                                    ),
                                    class_name="pb-4",
                                ),
                                key=category["id"],
                                class_name="border-b border-[var(--line)]",
                            ),
                        ),
                        disabled=CustomPlanState.busy | CustomPlanState.saved,
                        class_name="mt-8",
                    ),
                    rx.el.fieldset(
                        rx.el.legend(
                            "04 / Content & budget",
                            class_name="mb-5 text-xs font-semibold uppercase tracking-wider text-[var(--ink)]",
                        ),
                        rx.el.div(
                            number_field(
                                "posts", "Number of Posts / month", 1000
                            ),
                            number_field("reels", "Reels / month", 1000),
                            rx.foreach(REQUIREMENTS, requirement_select),
                            number_field(
                                "budget", "Monthly Budget (₹)", 10000000, 1
                            ),
                            class_name="grid grid-cols-1 gap-5 sm:grid-cols-2",
                        ),
                        rx.el.label(
                            "Message *",
                            html_for="custom-message",
                            class_name="mt-6 block text-xs font-semibold text-[var(--ink)]",
                        ),
                        rx.el.textarea(
                            id="custom-message",
                            name="message",
                            required=True,
                            max_length=5000,
                            rows=4,
                            placeholder="Your goals, audience, timeline and anything else we should know…",
                            class_name="mt-2 w-full rounded-lg border border-[var(--line)] bg-[var(--paper)] p-3 text-sm text-[var(--ink)] focus:outline-2 focus:outline-[#B79245]",
                        ),
                        disabled=CustomPlanState.busy | CustomPlanState.saved,
                        class_name="mt-8",
                    ),
                    rx.el.p(
                        CustomPlanState.message,
                        role="status",
                        aria_live="polite",
                        class_name=rx.cond(
                            CustomPlanState.saved,
                            "mt-5 rounded-lg border border-[var(--line)] bg-[var(--surface)] p-4 text-sm leading-6 text-[var(--ink)]",
                            "mt-5 text-sm leading-6 text-[var(--ink)]",
                        ),
                    ),
                    rx.el.button(
                        rx.cond(
                            CustomPlanState.busy,
                            "Saving enquiry…",
                            rx.cond(
                                CustomPlanState.saved,
                                "Enquiry saved",
                                "Send custom-plan enquiry",
                            ),
                        ),
                        type="submit",
                        disabled=CustomPlanState.busy | CustomPlanState.saved,
                        class_name="mt-5 flex min-h-12 w-full items-center justify-center rounded-full bg-[var(--primary)] px-5 py-3 text-sm font-semibold text-[var(--on-primary)] disabled:cursor-not-allowed disabled:opacity-60",
                    ),
                    on_submit=CustomPlanState.submit_enquiry,
                    reset_on_submit=False,
                    class_name="mt-8",
                ),
                class_name="mobile-drawer fixed left-1/2 top-1/2 z-[60] max-h-[90dvh] w-[calc(100%_-_2rem)] max-w-2xl -translate-x-1/2 -translate-y-1/2 overflow-y-auto rounded-2xl border border-[var(--line)] bg-[var(--paper)] p-5 font-['Inter'] text-[var(--ink)] outline-hidden sm:p-8",
            ),
        ),
    )
