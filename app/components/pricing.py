import reflex as rx

from app.content import PRICING, PLAN_FEATURE_NOTICE
from app.components.plan_forms import custom_plan_dialog
from app.states.pricing_state import PricingState, PricingCard


def plan_features(features: list[str], highlighted: bool) -> rx.Component:
    return rx.el.ul(
        rx.foreach(
            features,
            lambda feature: rx.el.li(
                rx.icon(
                    "check",
                    aria_hidden=True,
                    class_name=rx.cond(
                        highlighted,
                        "mt-0.5 h-4 w-4 shrink-0 text-[#D7BE82]",
                        "mt-0.5 h-4 w-4 shrink-0 text-[#79602C]",
                    ),
                ),
                rx.el.span(feature, class_name="min-w-0"),
                key=feature,
                class_name=rx.cond(
                    highlighted,
                    "flex items-start gap-2 py-1.5 text-xs leading-5 text-[#F7F2E7]",
                    "flex items-start gap-2 py-1.5 text-xs leading-5 text-[#153B2B]",
                ),
            ),
        ),
        class_name="mt-3",
    )


def plan_card(plan: PricingCard) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.h3(
                plan["name"],
                class_name=rx.cond(
                    plan["highlighted"],
                    "text-xl font-semibold text-[#F7F2E7]",
                    "text-xl font-semibold text-[#153B2B]",
                ),
            ),
            rx.cond(
                plan["highlighted"],
                rx.el.span(
                    "MOST POPULAR",
                    class_name="w-fit shrink-0 rounded-md bg-[#D7BE82] px-2 py-1 text-[8px] font-bold tracking-[0.08em] text-[#0C2A20]",
                ),
            ),
            class_name="flex min-w-0 flex-wrap items-center justify-between gap-2",
        ),
        rx.el.p(
            rx.el.span(
                f"₹{plan['total_inr']:,}",
                class_name="text-4xl font-semibold tracking-tight sm:text-[42px]",
            ),
            rx.el.span(
                rx.match(
                    PricingState.duration,
                    ("monthly", "/ month"),
                    ("six_months", "for 6 months"),
                    ("one_year", "per year"),
                    "",
                ),
                class_name=rx.cond(
                    plan["highlighted"],
                    "text-xs font-normal text-[#D8D0BD]",
                    "text-xs font-normal text-[#4E5C4D]",
                ),
            ),
            class_name=rx.cond(
                plan["highlighted"],
                "mt-5 flex flex-wrap items-baseline gap-x-2 gap-y-1 text-[#F7F2E7]",
                "mt-5 flex flex-wrap items-baseline gap-x-2 gap-y-1 text-[#153B2B]",
            ),
        ),
        rx.el.p(
            plan["description"],
            class_name=rx.cond(
                plan["highlighted"],
                "mt-3 text-xs leading-5 text-[#D8D0BD]",
                "mt-3 text-xs leading-5 text-[#4E5C4D]",
            ),
        ),
        rx.cond(
            plan["savings"] != "",
            rx.el.p(
                plan["savings"],
                class_name=rx.cond(
                    plan["highlighted"],
                    "mt-3 text-xs leading-5 text-[#D7BE82]",
                    "mt-3 text-xs leading-5 text-[#79602C]",
                ),
            ),
        ),
        rx.el.a(
            f"Choose {plan['name']}",
            rx.icon("arrow-up-right", class_name="h-4 w-4"),
            href=f"/checkout?plan={plan['id']}&duration={PricingState.duration}",
            class_name=rx.cond(
                plan["highlighted"],
                "mt-5 flex min-h-11 w-full items-center justify-center gap-3 rounded-lg bg-[#D7BE82] px-4 py-3 text-sm font-semibold text-[#0C2A20] hover:bg-[#E2CC9A] focus-visible:outline-2 focus-visible:outline-[#D7BE82]",
                "mt-5 flex min-h-11 w-full items-center justify-center gap-3 rounded-lg border border-[#153B2B] bg-transparent px-4 py-3 text-sm font-semibold text-[#153B2B] hover:bg-[#EEE5D3]",
            ),
        ),
        rx.el.p(
            "MONTHLY DELIVERABLES",
            class_name=rx.cond(
                plan["highlighted"],
                "mt-5 border-t border-[#355547] pt-4 text-[9px] font-semibold tracking-[0.14em] text-[#D7BE82]",
                "mt-5 border-t border-[#D9CFBB] pt-4 text-[9px] font-semibold tracking-[0.14em] text-[#4E5C4D]",
            ),
        ),
        plan_features(plan["features"][:6], plan["highlighted"]),
        rx.cond(
            plan["features"].length() > 6,
            rx.el.details(
                rx.el.summary(
                    "View All Features",
                    rx.icon(
                        "chevron-down",
                        aria_hidden=True,
                        class_name="h-4 w-4 shrink-0 transition-transform group-open:rotate-180",
                    ),
                    aria_label=f"View All Features for {plan['name']}",
                    class_name=rx.cond(
                        plan["highlighted"],
                        "flex min-h-11 cursor-pointer list-none items-center justify-between gap-2 py-3 text-xs font-semibold text-[#F7F2E7]",
                        "flex min-h-11 cursor-pointer list-none items-center justify-between gap-2 py-3 text-xs font-semibold text-[#153B2B]",
                    ),
                ),
                plan_features(plan["features"][6:], plan["highlighted"]),
                class_name=rx.cond(
                    plan["highlighted"],
                    "group mt-3 border-t border-[#355547]",
                    "group mt-3 border-t border-[#D9CFBB]",
                ),
            ),
        ),
        key=plan["id"],
        class_name=rx.cond(
            plan["highlighted"],
            "flex min-w-0 w-full flex-col rounded-xl border border-[#B79245] bg-[#153B2B] p-5 sm:p-6",
            "flex min-w-0 w-full flex-col rounded-xl border border-[#D9CFBB] bg-[#F7F2E7] p-5 sm:p-6",
        ),
    )


def pricing() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Choose Your",
                rx.el.br(),
                rx.el.span(
                    "Growth Plan",
                    class_name="font-['Playfair_Display'] font-normal text-[#B79245]",
                ),
                class_name="text-[28px] font-medium leading-tight tracking-[-0.035em] text-[var(--ink)] sm:text-[32px] lg:text-[34px]",
            ),
            rx.el.p(
                "A focused start or a fuller creative partnership. Compare the sample scopes, then choose the support that fits your next chapter.",
                class_name="mt-4 max-w-2xl text-sm leading-7 text-[var(--muted)]",
            ),
            class_name="mb-7 min-w-0",
        ),
        rx.el.div(
            rx.icon(
                "info", class_name="mt-1 h-5 w-5 shrink-0 text-[var(--ink)]"
            ),
            rx.el.div(
                rx.el.p(
                    "SAMPLE PRICING · NOT AN APPROVED OFFER",
                    class_name="text-[10px] font-semibold tracking-wider text-[var(--ink)]",
                ),
                rx.el.p(
                    PRICING["notice"],
                    class_name="mt-2 text-xs leading-6 text-[var(--muted)]",
                ),
                rx.el.p(
                    "Payments are held until the owner confirms commercial terms. MOST POPULAR is a draft plan highlight, not a verified sales claim.",
                    class_name="mt-2 text-xs leading-6 text-[var(--muted)]",
                ),
            ),
            class_name="mb-8 flex gap-3 rounded-xl border border-[var(--line)] bg-[var(--surface)] p-5",
        ),
        rx.el.p(
            "One total for the selected duration. Not a monthly instalment. No automatic discounts are applied.",
            class_name="mb-4 text-xs leading-6 text-[var(--muted)]",
        ),
        rx.el.div(
            rx.foreach(
                PRICING["durations"],
                lambda duration: rx.el.button(
                    duration["label"],
                    type="button",
                    on_click=lambda: PricingState.select_duration(
                        duration["id"]
                    ),
                    aria_pressed=PricingState.duration == duration["id"],
                    aria_controls="pricing-cards",
                    key=duration["id"],
                    class_name=rx.cond(
                        PricingState.duration == duration["id"],
                        "min-h-11 min-w-0 flex-1 whitespace-nowrap rounded-lg bg-[#153B2B] px-2 py-2 text-xs font-semibold text-[#F7F2E7] sm:px-4 sm:text-sm",
                        "min-h-11 min-w-0 flex-1 whitespace-nowrap rounded-lg bg-transparent px-2 py-2 text-xs font-medium text-[#153B2B] hover:bg-[#EEE5D3] sm:px-4 sm:text-sm",
                    ),
                ),
            ),
            role="group",
            aria_label="Pricing duration",
            class_name="mx-auto mb-5 flex w-full max-w-sm gap-1 rounded-xl border border-[#D9CFBB] bg-[#F7F2E7] p-1",
        ),
        rx.el.div(
            rx.foreach(PricingState.cards, plan_card),
            id="pricing-cards",
            aria_live="polite",
            class_name="grid w-full grid-cols-1 items-start gap-5 lg:grid-cols-3",
        ),
        rx.el.p(
            PLAN_FEATURE_NOTICE,
            class_name="mt-7 text-xs leading-6 text-[var(--muted)]",
        ),
        rx.el.div(
            rx.el.h3(
                "Available as add-ons",
                class_name="text-base font-semibold text-[var(--ink)]",
            ),
            rx.el.ul(
                rx.foreach(
                    [
                        ("camera", "Product / Brand Photography"),
                        ("video", "Professional Video Shoot"),
                        ("megaphone", "Paid Ads Management"),
                        ("users", "Influencer Marketing"),
                        ("palette", "Logo / Branding"),
                        ("globe", "Website / SEO"),
                    ],
                    lambda addon: rx.el.li(
                        rx.icon(
                            addon[0],
                            aria_hidden=True,
                            class_name="h-5 w-5 shrink-0 text-[var(--display)]",
                        ),
                        rx.el.span(
                            addon[1],
                            class_name="min-w-0 text-xs font-medium leading-5 text-[var(--ink)]",
                        ),
                        key=addon[1],
                        class_name="flex min-w-0 flex-col items-start gap-2 rounded-lg border border-[var(--line)] bg-[var(--surface)] p-3 sm:flex-row sm:items-center sm:gap-3 sm:p-4",
                    ),
                ),
                class_name="mt-4 grid w-full grid-cols-2 gap-3 lg:grid-cols-3",
            ),
            class_name="mt-8 min-w-0",
        ),
        rx.el.div(
            rx.el.p(
                "Quoted separately / excluded from sample totals",
                class_name="text-xs font-semibold text-[var(--ink)]",
            ),
            rx.el.ul(
                rx.foreach(
                    PRICING["exclusions"],
                    lambda item: rx.el.li(
                        rx.icon("minus", class_name="h-3 w-3 shrink-0"),
                        item,
                        key=item,
                        class_name="flex items-center gap-2 text-xs leading-6 text-[var(--muted)]",
                    ),
                ),
                class_name="mt-3 grid gap-x-6 sm:grid-cols-2",
            ),
            rx.el.p(
                PRICING["tax_notice"],
                class_name="mt-4 text-xs leading-6 text-[var(--muted)]",
            ),
            class_name="mt-6 border-t border-[var(--line)] pt-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "NOT QUITE YOUR FIT?",
                    class_name="text-[10px] font-semibold tracking-wider text-[var(--muted)]",
                ),
                rx.el.h3(
                    PRICING["custom_plan_title"],
                    class_name="mt-3 font-['Playfair_Display'] text-2xl text-[var(--ink)]",
                ),
                rx.el.p(
                    PRICING["custom_plan_description"],
                    class_name="mt-3 max-w-xl text-sm leading-7 text-[var(--muted)]",
                ),
            ),
            custom_plan_dialog(),
            class_name="mt-10 flex flex-col items-start gap-6 rounded-xl border border-[var(--line)] bg-[var(--surface)] p-6 sm:p-8 lg:flex-row lg:items-center lg:justify-between",
        ),
        id="plans",
        class_name="mx-auto w-full max-w-[1280px] border-t border-[var(--line)] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )
