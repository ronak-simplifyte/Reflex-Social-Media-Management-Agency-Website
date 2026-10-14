import reflex as rx

from app.content import (
    BENEFITS,
    BEFORE_AFTER,
    BEFORE_AFTER_NOTICE,
    BUSINESS,
    LEGAL_LINKS,
    WHATSAPP_VERIFIED,
    verified_link,
    FAQS,
    INDUSTRIES,
    PLATFORMS,
    PROCESS_STEPS,
    TESTIMONIALS,
    EditorialItem,
    PortfolioContent,
    ServiceContent,
)
from app.components.navigation import NAVIGATION, brand
from app.states.home_state import HomeState


SERVICE_TABS: list[str] = [
    "Content",
    "Management",
    "Strategy",
    "Growth",
    "Creative",
]
WORK_FILTERS: list[str] = [
    "All",
    "Instagram",
    "Reels",
    "Branding",
    "LinkedIn",
    "Facebook",
    "YouTube",
]
SOCIAL_LINKS: list[tuple[str, str, bool, bool]] = [
    (link["label"], link["url"], verified_link(link), link["is_placeholder"])
    for link in BUSINESS["social_links"].values()
]
PAIN_POINTS: list[str] = [
    "You’re posting, but there’s no clear direction.",
    "Your visuals don’t quite feel like your brand.",
    "Content keeps slipping to the bottom of the list.",
    "You’re on every platform, without a plan for any.",
    "The numbers are there. The context isn’t.",
]


def section_heading(
    number: str, label: str, title: str, accent: str, description: str
) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            number,
            rx.el.span(class_name="h-px w-8 bg-[#B79245]"),
            label,
            class_name="mb-5 flex items-center gap-3 text-[10px] font-semibold uppercase tracking-[0.18em] text-[var(--muted)]",
        ),
        rx.el.h2(
            title,
            " ",
            rx.el.em(
                accent,
                class_name="font-['Playfair_Display'] font-normal text-[var(--display)]",
            ),
            class_name="max-w-3xl text-3xl font-medium leading-tight tracking-[-0.035em] text-[var(--ink)] sm:text-4xl lg:text-[42px]",
        ),
        rx.el.p(
            description,
            class_name="mt-4 max-w-2xl text-sm leading-7 text-[var(--muted)] sm:text-base",
        ),
        class_name="mb-9 min-w-0 sm:mb-12",
    )


def platforms() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "THE RIGHT CHANNELS. ONE COHERENT BRAND.",
                    class_name="text-[10px] font-semibold tracking-[0.18em] text-[var(--muted)]",
                ),
                rx.el.p(
                    "Meet your audience where they are.",
                    class_name="mt-3 font-['Playfair_Display'] text-2xl text-[var(--ink)]",
                ),
                class_name="mb-7 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    PLATFORMS,
                    lambda platform: rx.el.article(
                        rx.match(
                            platform["id"],
                            (
                                "instagram",
                                rx.icon(
                                    "camera",
                                    class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                                ),
                            ),
                            (
                                "facebook",
                                rx.icon(
                                    "notebook_pen",
                                    class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                                ),
                            ),
                            (
                                "linkedin",
                                rx.icon(
                                    "external_link",
                                    class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                                ),
                            ),
                            (
                                "youtube",
                                rx.icon(
                                    "layout_dashboard",
                                    class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                                ),
                            ),
                            (
                                "x",
                                rx.icon(
                                    "message-circle",
                                    class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                                ),
                            ),
                            (
                                "pinterest",
                                rx.icon(
                                    "pin",
                                    class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                                ),
                            ),
                            rx.icon(
                                "map-pin",
                                class_name="mb-4 h-6 w-6 text-[var(--ink)]",
                            ),
                        ),
                        rx.el.h3(
                            platform["name"],
                            class_name="text-sm font-semibold leading-snug text-[var(--ink)]",
                        ),
                        rx.el.p(
                            platform["description"],
                            class_name="mt-3 text-xs leading-6 text-[var(--muted)]",
                        ),
                        rx.el.p(
                            platform["formats"].join(" · "),
                            class_name="mt-4 text-[10px] leading-5 text-[var(--muted)]",
                        ),
                        key=platform["id"],
                        class_name="min-w-0 border-t border-[var(--line)] pt-6",
                    ),
                ),
                class_name="grid grid-cols-1 gap-6 min-[420px]:grid-cols-2 md:grid-cols-4 xl:grid-cols-7",
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 py-12 sm:px-6 lg:px-10",
        ),
        aria_label="Supported platforms",
        class_name="w-full bg-[var(--paper)]",
    )


def problems_solution() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                section_heading(
                    "01",
                    "Sound familiar?",
                    "More posting isn’t",
                    "always the answer.",
                    "When social becomes another thing to keep up with, it’s easy to lose the bigger picture.",
                ),
                rx.el.ul(
                    rx.foreach(
                        PAIN_POINTS,
                        lambda point: rx.el.li(
                            rx.icon(
                                "minus",
                                class_name="h-4 w-4 shrink-0 text-[var(--display)]",
                            ),
                            point,
                            class_name="flex items-start gap-3 border-b border-[var(--line)] py-4 text-sm leading-6 text-[var(--muted)]",
                            key=point,
                        ),
                    )
                ),
                class_name="min-w-0",
            ),
            rx.el.div(
                rx.icon(
                    "sprout",
                    class_name="mb-8 h-10 w-10 stroke-[1] text-[#D7BE82]",
                ),
                rx.el.p(
                    "LESS NOISE. MORE PURPOSE.",
                    class_name="text-[10px] tracking-[0.2em] text-[#D7BE82]",
                ),
                rx.el.h3(
                    "A thoughtful plan.",
                    rx.el.br(),
                    rx.el.em(
                        "A meaningful presence.",
                        class_name="font-['Playfair_Display'] font-normal",
                    ),
                    class_name="mt-5 text-3xl font-medium leading-tight tracking-tight text-[#F7F2E7] sm:text-4xl",
                ),
                rx.el.p(
                    "We connect the strategy, the creative and the everyday care. A clear direction for your channels, content that sounds like you, and a workflow you can actually follow.",
                    class_name="mt-6 text-sm leading-7 text-[#D8D0BD]",
                ),
                rx.el.a(
                    "Find your direction",
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    href="#services",
                    class_name="mt-8 inline-flex min-h-12 items-center gap-4 border-b border-[#D7BE82] py-3 text-sm text-[#F7F2E7]",
                ),
                class_name="min-w-0 rounded-t-[60px] bg-[#153B2B] p-7 sm:p-10 lg:mt-8 lg:p-12",
            ),
            class_name="mx-auto grid w-full max-w-[1280px] gap-10 px-5 py-16 sm:px-6 lg:grid-cols-2 lg:gap-20 lg:px-10 lg:py-24",
        ),
        class_name="w-full bg-[var(--surface)]",
    )


def service_card(service: ServiceContent, index: int) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.span(
                f"0{index + 1}",
                class_name="font-['Playfair_Display'] text-xl text-[var(--display)]",
            ),
            rx.icon("arrow-up-right", class_name="h-4 w-4 text-[var(--muted)]"),
            class_name="mb-6 flex items-center justify-between",
        ),
        rx.el.h3(
            service["title"],
            class_name="text-base font-semibold leading-snug text-[var(--ink)]",
        ),
        rx.el.p(
            service["description"],
            class_name="mt-3 text-sm leading-7 text-[var(--muted)]",
        ),
        key=service["id"],
        class_name="min-w-0 border border-[var(--line)] p-6 transition-colors hover:bg-[var(--surface)]",
    )


def services() -> rx.Component:
    return rx.el.section(
        section_heading(
            "02",
            "What we do",
            "The thinking. The making.",
            "The managing.",
            "Choose the support your brand needs. Every service is scoped with you — not every service is included in every plan.",
        ),
        rx.el.div(
            rx.foreach(
                SERVICE_TABS,
                lambda tab: rx.el.button(
                    tab,
                    on_click=lambda: HomeState.select_service(tab),
                    type="button",
                    aria_pressed=HomeState.service_tab == tab,
                    aria_controls="service-panel",
                    class_name=rx.cond(
                        HomeState.service_tab == tab,
                        "min-h-12 rounded-full bg-[var(--primary)] px-5 py-3 text-sm font-medium text-[var(--on-primary)]",
                        "min-h-12 rounded-full border border-[var(--line)] bg-transparent px-5 py-3 text-sm font-medium text-[var(--ink)] hover:bg-[var(--surface)]",
                    ),
                    key=tab,
                ),
            ),
            role="group",
            aria_label="Service categories",
            class_name="mb-7 flex flex-wrap gap-2",
        ),
        rx.el.div(
            rx.el.p(
                HomeState.service_description,
                class_name="mb-6 text-sm text-[var(--muted)]",
            ),
            rx.el.div(
                rx.foreach(HomeState.active_services, service_card),
                class_name="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3",
            ),
            id="service-panel",
            aria_live="polite",
            aria_label=f"{HomeState.service_tab} services",
        ),
        id="services",
        class_name="mx-auto w-full max-w-[1280px] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )


def process() -> rx.Component:
    return rx.el.section(
        section_heading(
            "03",
            "How it works",
            "Good work starts with",
            "a clear process.",
            "From the first conversation to the next content cycle, you know what’s happening and what comes next.",
        ),
        rx.el.ol(
            rx.foreach(
                PROCESS_STEPS,
                lambda step, index: rx.el.li(
                    rx.el.div(
                        rx.el.span(
                            f"0{index + 1}",
                            class_name="flex h-12 w-12 items-center justify-center rounded-full border border-[var(--line)] bg-[var(--surface)] font-['Playfair_Display'] text-xl text-[var(--ink)]",
                        ),
                        rx.el.div(class_name="h-px flex-1 bg-[var(--line)]"),
                        class_name="mb-6 flex items-center gap-4",
                    ),
                    rx.icon(
                        step["icon"],
                        class_name="mb-4 h-5 w-5 text-[var(--display)]",
                    ),
                    rx.el.h3(
                        step["title"],
                        class_name="text-base font-semibold text-[var(--ink)]",
                    ),
                    rx.el.p(
                        step["description"],
                        class_name="mt-3 text-sm leading-7 text-[var(--muted)]",
                    ),
                    key=step["id"],
                    class_name="min-w-0",
                ),
            ),
            class_name="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4",
        ),
        id="process",
        class_name="mx-auto w-full max-w-[1280px] border-t border-[var(--line)] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )


def concept_art(project: PortfolioContent) -> rx.Component:
    return rx.el.div(
        rx.match(
            project["id"],
            (
                "cafe_concept",
                rx.el.div(
                    rx.el.p(
                        "THE DAILY RITUAL",
                        class_name="text-[9px] tracking-[0.2em]",
                    ),
                    rx.icon("coffee", class_name="my-5 h-14 w-14 stroke-[1]"),
                    rx.el.p(
                        "Brewed slowly.",
                        class_name="font-['Playfair_Display'] text-3xl",
                    ),
                    rx.el.p(
                        "Shared warmly.",
                        class_name="font-['Playfair_Display'] text-3xl italic",
                    ),
                    rx.el.p(
                        "CAFÉ · EDITORIAL CONCEPT",
                        class_name="mt-6 text-[8px] tracking-[0.15em]",
                    ),
                    class_name="flex h-full flex-col items-center justify-center bg-[#D7BE82] p-5 text-center text-[#153B2B]",
                ),
            ),
            (
                "wellness_concept",
                rx.el.div(
                    rx.el.p(
                        "ROOM TO BREATHE",
                        class_name="text-[9px] tracking-[0.2em]",
                    ),
                    rx.icon("flower-2", class_name="my-5 h-14 w-14 stroke-[1]"),
                    rx.el.p(
                        "Find your",
                        class_name="font-['Playfair_Display'] text-3xl",
                    ),
                    rx.el.p(
                        "own rhythm.",
                        class_name="font-['Playfair_Display'] text-3xl italic",
                    ),
                    rx.el.p(
                        "WELLNESS · VISUAL CONCEPT",
                        class_name="mt-6 text-[8px] tracking-[0.15em]",
                    ),
                    class_name="flex h-full flex-col items-center justify-center bg-[#EEE5D3] p-5 text-center text-[#153B2B]",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "IDEAS, MADE CLEAR",
                    class_name="text-[9px] tracking-[0.2em] text-[#D7BE82]",
                ),
                rx.icon(
                    "shapes",
                    class_name="my-5 h-14 w-14 stroke-[1] text-[#D7BE82]",
                ),
                rx.el.p(
                    "Expertise meets",
                    class_name="font-['Playfair_Display'] text-3xl",
                ),
                rx.el.p(
                    "understanding.",
                    class_name="font-['Playfair_Display'] text-3xl italic",
                ),
                rx.el.p(
                    "B2B · EDITORIAL CONCEPT",
                    class_name="mt-6 text-[8px] tracking-[0.15em] text-[#D7BE82]",
                ),
                class_name="flex h-full flex-col items-center justify-center bg-[#153B2B] p-5 text-center text-[#F7F2E7]",
            ),
        ),
        role="img",
        aria_label=project["image_alt"],
        class_name="h-72 w-full overflow-hidden rounded-t-[48px]",
    )


def portfolio_card(project: PortfolioContent) -> rx.Component:
    return rx.el.article(
        concept_art(project),
        rx.el.p(
            project["demo_label"],
            class_name="mt-5 w-fit border border-[var(--line)] px-2 py-1 text-[10px] font-medium text-[var(--muted)]",
        ),
        rx.el.h3(
            project["title"],
            class_name="mt-3 text-lg font-semibold leading-snug text-[var(--ink)]",
        ),
        rx.el.p(
            project["industry"], class_name="mt-2 text-xs text-[var(--muted)]"
        ),
        rx.el.p(
            project["brief"],
            class_name="mt-4 text-sm leading-6 text-[var(--muted)]",
        ),
        rx.el.p(
            project["approach"],
            class_name="mt-3 text-sm leading-6 text-[var(--muted)]",
        ),
        rx.el.ul(
            rx.foreach(
                project["deliverables"],
                lambda deliverable: rx.el.li(
                    rx.icon("check", class_name="mt-1 h-3 w-3 shrink-0"),
                    deliverable,
                    key=deliverable,
                    class_name="flex gap-2 text-xs leading-6 text-[var(--muted)]",
                ),
            ),
            class_name="mt-4",
        ),
        rx.el.p(
            project["disclaimer"],
            class_name="mt-4 border-t border-[var(--line)] pt-3 text-[10px] leading-5 text-[var(--muted)]",
        ),
        key=project["id"],
        class_name="min-w-0",
    )


def portfolio() -> rx.Component:
    return rx.el.section(
        section_heading(
            "04",
            "The creative edit",
            "A glimpse of",
            "what’s possible.",
            "Conceptual demo work, created to explore direction and craft. These are fictional briefs — not client case studies or evidence of results.",
        ),
        rx.el.div(
            rx.foreach(
                WORK_FILTERS,
                lambda category: rx.el.button(
                    category,
                    type="button",
                    on_click=lambda: HomeState.select_portfolio(category),
                    aria_pressed=HomeState.portfolio_filter == category,
                    aria_controls="portfolio-results",
                    key=category,
                    class_name=rx.cond(
                        HomeState.portfolio_filter == category,
                        "min-h-11 rounded-full bg-[var(--primary)] px-4 py-3 text-xs font-medium text-[var(--on-primary)]",
                        "min-h-11 rounded-full border border-[var(--line)] px-4 py-3 text-xs font-medium text-[var(--ink)] hover:bg-[var(--surface)]",
                    ),
                ),
            ),
            role="group",
            aria_label="Filter conceptual work",
            class_name="mb-8 flex flex-wrap gap-2",
        ),
        rx.el.div(
            rx.foreach(HomeState.visible_portfolio, portfolio_card),
            id="portfolio-results",
            aria_live="polite",
            aria_label=f"{HomeState.portfolio_filter} conceptual projects",
            class_name="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3",
        ),
        id="work",
        class_name="mx-auto w-full max-w-[1280px] border-t border-[var(--line)] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )


def industries() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_heading(
                "05",
                "Different worlds. Same care.",
                "Your industry.",
                "Your own story.",
                "Every audience has its own language. We start by understanding yours, then shape the channels and content around it.",
            ),
            rx.el.div(
                rx.foreach(
                    INDUSTRIES,
                    lambda industry: rx.el.div(
                        rx.icon(
                            industry["icon"],
                            class_name="h-5 w-5 shrink-0 text-[var(--display)]",
                        ),
                        rx.el.span(
                            industry["label"],
                            class_name="text-sm font-medium leading-6 text-[var(--ink)]",
                        ),
                        key=industry["id"],
                        class_name="flex min-w-0 items-center gap-3 border-b border-[var(--line)] py-5",
                    ),
                ),
                class_name="grid grid-cols-1 gap-x-8 sm:grid-cols-2 lg:grid-cols-4",
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
        ),
        class_name="w-full bg-[var(--surface)]",
    )


def benefit_card(item: EditorialItem) -> rx.Component:
    return rx.el.article(
        rx.icon(
            item["icon"],
            class_name="mb-5 h-6 w-6 stroke-[1.5] text-[var(--display)]",
        ),
        rx.el.h3(
            item["title"], class_name="text-lg font-semibold text-[var(--ink)]"
        ),
        rx.el.p(
            item["description"],
            class_name="mt-3 text-sm leading-7 text-[var(--muted)]",
        ),
        key=item["id"],
        class_name="min-w-0 border-t border-[var(--line)] pt-6",
    )


def benefits_about() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                section_heading(
                    "06",
                    "Our approach",
                    "Small details.",
                    "Considered together.",
                    "The Social Atelier is a draft agency identity built around a simple approach: understand the business, make a clear plan, and create with care.",
                ),
                rx.el.p(
                    "We believe in fewer assumptions and better conversations. Audience research shapes the direction. A shared calendar makes room for feedback. Content is published only after approval, and reporting puts the available numbers in context.",
                    class_name="max-w-2xl text-sm leading-7 text-[var(--muted)]",
                ),
                rx.el.p(
                    "No invented milestones. No promises of overnight growth. Just an approach grounded in clear responsibilities, thoughtful creative and continuous learning.",
                    class_name="mt-5 max-w-2xl text-sm leading-7 text-[var(--muted)]",
                ),
                rx.el.a(
                    "See the process",
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    href="#process",
                    class_name="mt-6 inline-flex min-h-12 items-center gap-3 border-b border-[var(--line)] text-sm font-medium text-[var(--ink)]",
                ),
                class_name="min-w-0",
            ),
            rx.el.div(
                rx.el.span(
                    "WHY THIS APPROACH",
                    class_name="text-[10px] tracking-[0.2em] text-[var(--muted)]",
                ),
                rx.el.div(
                    rx.el.p("Not just more content."),
                    rx.el.p("More intention.", class_name="italic"),
                    class_name="mt-7 font-['Playfair_Display'] text-4xl leading-tight text-[var(--ink)]",
                ),
                rx.icon(
                    "sprout",
                    class_name="mt-8 h-16 w-16 stroke-[1] text-[var(--display)]",
                ),
                class_name="flex min-w-0 flex-col justify-center rounded-t-full border border-[var(--line)] bg-[var(--surface)] p-8 text-center sm:p-12 lg:min-h-80",
            ),
            class_name="grid gap-10 lg:grid-cols-[1.4fr_1fr] lg:gap-20",
        ),
        rx.el.div(
            rx.foreach(BENEFITS, benefit_card),
            class_name="mt-14 grid grid-cols-1 gap-x-8 gap-y-10 md:grid-cols-2 lg:grid-cols-3",
        ),
        id="about",
        class_name="mx-auto w-full max-w-[1280px] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )


def comparison() -> rx.Component:
    return rx.el.section(
        section_heading(
            "07",
            "A more intentional workflow",
            "From scattered efforts",
            "to shared direction.",
            BEFORE_AFTER_NOTICE,
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "WITHOUT A SHARED PLAN",
                    class_name="text-[10px] font-semibold tracking-wider text-[var(--muted)]",
                ),
                rx.el.span(
                    "WITH AN AGREED WORKFLOW",
                    class_name="text-[10px] font-semibold tracking-wider text-[var(--ink)]",
                ),
                class_name="hidden grid-cols-2 gap-10 border-b border-[var(--line)] pb-5 sm:grid",
            ),
            rx.foreach(
                BEFORE_AFTER,
                lambda row: rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            row["topic"],
                            class_name="text-[10px] font-semibold uppercase tracking-wider text-[var(--muted)]",
                        ),
                        rx.el.p(
                            rx.icon(
                                "minus", class_name="mt-1 h-4 w-4 shrink-0"
                            ),
                            row["before"],
                            class_name="mt-3 flex gap-3 text-sm leading-6 text-[var(--muted)]",
                        ),
                        class_name="min-w-0",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "WITH A PLAN",
                            class_name="text-[10px] font-semibold tracking-wider text-[var(--ink)] sm:hidden",
                        ),
                        rx.el.p(
                            rx.icon(
                                "check",
                                class_name="mt-1 h-4 w-4 shrink-0 text-[var(--display)]",
                            ),
                            row["after"],
                            class_name="flex gap-3 text-sm leading-6 text-[var(--ink)]",
                        ),
                        class_name="min-w-0",
                    ),
                    key=row["id"],
                    class_name="grid grid-cols-1 items-center gap-4 border-b border-[var(--line)] py-6 sm:grid-cols-2 sm:gap-10",
                ),
            ),
            class_name="w-full",
        ),
        class_name="mx-auto w-full max-w-[1280px] border-t border-[var(--line)] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
    )


def testimonials() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_heading(
                "08",
                "Illustrative voices",
                "What a thoughtful workflow",
                "could feel like.",
                "The following are demo testimonial examples only. They are fictional quotations, not verified people, endorsements or customer feedback.",
            ),
            rx.el.div(
                rx.foreach(
                    TESTIMONIALS,
                    lambda testimonial: rx.el.figure(
                        rx.icon(
                            "quote",
                            class_name="mb-6 h-7 w-7 stroke-[1] text-[var(--display)]",
                        ),
                        rx.el.p(
                            testimonial["demo_label"],
                            class_name="mb-5 text-[10px] font-semibold text-[var(--muted)]",
                        ),
                        rx.el.blockquote(
                            testimonial["quote"],
                            class_name="font-['Playfair_Display'] text-xl leading-relaxed text-[var(--ink)]",
                        ),
                        rx.el.figcaption(
                            rx.el.p(
                                testimonial["attribution"],
                                class_name="mt-6 text-sm font-medium text-[var(--ink)]",
                            ),
                            rx.el.p(
                                testimonial["role"],
                                class_name="mt-1 text-xs text-[var(--muted)]",
                            ),
                            rx.el.p(
                                testimonial["disclaimer"],
                                class_name="mt-4 text-[10px] leading-5 text-[var(--muted)]",
                            ),
                        ),
                        key=testimonial["id"],
                        class_name="min-w-0 border-t border-[var(--line)] pt-6",
                    ),
                ),
                class_name="grid grid-cols-1 gap-8 md:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 py-16 sm:px-6 lg:px-10 lg:py-24",
        ),
        class_name="w-full bg-[var(--surface)]",
    )


def faqs() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_heading(
                "09",
                "A few things, answered",
                "Good questions.",
                "Clear answers.",
                "Scope, approvals, expectations and what’s still in draft. Here’s what to know before getting started.",
            ),
            class_name="min-w-0",
        ),
        rx.el.div(
            rx.foreach(
                FAQS,
                lambda faq: rx.el.details(
                    rx.el.summary(
                        rx.el.span(
                            faq["question"],
                            class_name="min-w-0 text-sm font-medium leading-6",
                        ),
                        rx.icon(
                            "plus",
                            class_name="faq-plus h-4 w-4 shrink-0 transition-transform",
                        ),
                        class_name="flex min-h-14 cursor-pointer list-none items-center justify-between gap-4 py-5 text-[var(--ink)]",
                    ),
                    rx.el.p(
                        faq["answer"],
                        class_name="pb-6 pr-5 text-sm leading-7 text-[var(--muted)]",
                    ),
                    key=faq["id"],
                    class_name="border-b border-[var(--line)]",
                ),
            ),
            class_name="min-w-0",
        ),
        id="faq",
        class_name="mx-auto grid w-full max-w-[1280px] gap-6 border-t border-[var(--line)] px-5 py-16 sm:px-6 lg:grid-cols-[0.8fr_1.2fr] lg:gap-20 lg:px-10 lg:py-24",
    )


def contact_cta() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.icon(
                "sparkles",
                class_name="mx-auto mb-7 h-7 w-7 stroke-[1] text-[#D7BE82]",
            ),
            rx.el.p(
                "YOUR NEXT CHAPTER",
                class_name="text-[10px] tracking-[0.2em] text-[#D7BE82]",
            ),
            rx.el.h2(
                "Your Next Post Shouldn’t Be",
                " ",
                rx.el.em(
                    "Another Pending Task.",
                    class_name="font-['Playfair_Display'] font-normal",
                ),
                class_name="mt-5 text-4xl font-medium leading-tight tracking-tight text-[#F7F2E7] sm:text-5xl",
            ),
            rx.el.p(
                "Let one team take care of your social media.",
                class_name="mx-auto mt-6 max-w-lg text-sm leading-7 text-[#D8D0BD]",
            ),
            rx.el.a(
                "Choose Your Plan",
                rx.icon("arrow-up-right", class_name="h-4 w-4"),
                href="/#plans",
                class_name="mx-auto mt-8 flex min-h-12 w-fit items-center justify-center gap-3 rounded-full bg-[#D7BE82] px-7 py-3 text-sm font-semibold text-[#0C2A20] hover:opacity-90",
            ),
            rx.cond(
                WHATSAPP_VERIFIED,
                rx.el.a(
                    rx.icon("message-circle", class_name="h-4 w-4"),
                    "Talk on WhatsApp",
                    href=BUSINESS["contact_links"]["whatsapp"]["url"],
                    class_name="mx-auto mt-4 flex min-h-12 w-fit items-center justify-center gap-3 rounded-full border border-[#D7BE82] px-7 py-3 text-sm font-semibold text-[#F7F2E7]",
                ),
                rx.el.div(
                    rx.el.a(
                        "Tell us what you need",
                        rx.icon("arrow-up-right", class_name="h-4 w-4"),
                        href="/#contact",
                        class_name="mx-auto mt-4 flex min-h-12 w-fit items-center justify-center gap-3 border-b border-[#D7BE82] px-3 py-3 text-sm font-medium text-[#F7F2E7]",
                    ),
                    rx.el.p(
                        "Enquiries can be saved now. Direct WhatsApp is pending verification. Payments remain on hold until the owner verifies business terms and payment setup.",
                        class_name="mx-auto mt-5 max-w-md text-xs leading-6 text-[#D8D0BD]",
                    ),
                ),
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 py-16 text-center sm:px-6 lg:px-10 lg:py-24",
        ),
        aria_label="Your next step",
        class_name="w-full bg-[#0C2A20]",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    brand(),
                    rx.el.p(
                        BUSINESS["tagline"],
                        class_name="mt-5 text-sm leading-7 text-[var(--muted)]",
                    ),
                    rx.el.p(
                        BUSINESS["placeholder_notice"],
                        class_name="mt-4 max-w-sm text-xs leading-6 text-[var(--muted)]",
                    ),
                    class_name="min-w-0",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Explore",
                        class_name="mb-4 text-xs font-semibold text-[var(--ink)]",
                    ),
                    rx.el.nav(
                        rx.foreach(
                            NAVIGATION,
                            lambda item: rx.el.a(
                                item["label"],
                                href=item["href"],
                                key=item["href"],
                                class_name="flex min-h-11 items-center text-xs text-[var(--muted)] hover:text-[var(--ink)]",
                            ),
                        ),
                        aria_label="Footer navigation",
                        class_name="flex flex-col",
                    ),
                    class_name="min-w-0",
                ),
                rx.el.div(
                    rx.el.h3(
                        "The details",
                        class_name="mb-4 text-xs font-semibold text-[var(--ink)]",
                    ),
                    rx.el.a(
                        "Frequently asked questions",
                        href="/#faq",
                        class_name="flex min-h-11 items-center text-xs text-[var(--muted)]",
                    ),
                    rx.el.a(
                        "Our approach",
                        href="/#about",
                        class_name="flex min-h-11 items-center text-xs text-[var(--muted)]",
                    ),
                    rx.el.a(
                        "Contact & availability",
                        href="/#contact",
                        class_name="flex min-h-11 items-center text-xs text-[var(--muted)]",
                    ),
                    rx.foreach(
                        LEGAL_LINKS,
                        lambda link: rx.el.a(
                            link[0],
                            href=link[1],
                            key=link[1],
                            class_name="flex min-h-11 items-center text-xs text-[var(--muted)] hover:text-[var(--ink)]",
                        ),
                    ),
                    rx.el.p(
                        "Legal policies are drafts pending owner approval. Payments stay on hold until commercial terms and payment setup are verified. Enquiries are not orders.",
                        class_name="mt-4 text-xs leading-6 text-[var(--muted)]",
                    ),
                    class_name="min-w-0",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Stay connected",
                        class_name="mb-4 text-xs font-semibold text-[var(--ink)]",
                    ),
                    rx.foreach(
                        SOCIAL_LINKS,
                        lambda link: rx.cond(
                            link[2] & ~link[3],
                            rx.el.a(
                                link[0],
                                href=link[1],
                                class_name="flex min-h-11 items-center text-xs text-[var(--muted)]",
                            ),
                            rx.el.p(
                                link[0],
                                rx.el.span(
                                    " · placeholder, pending verification",
                                    class_name="text-[10px]",
                                ),
                                class_name="py-2 text-xs text-[var(--muted)]",
                            ),
                        ),
                    ),
                    rx.el.a(
                        rx.icon("message-circle", class_name="h-4 w-4"),
                        "Contact information",
                        href="#contact",
                        class_name="mt-4 flex min-h-11 items-center gap-2 text-xs font-medium text-[var(--ink)]",
                    ),
                    class_name="min-w-0",
                ),
                class_name="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-[1.6fr_0.8fr_1fr_1fr]",
            ),
            rx.el.div(
                rx.el.p(
                    "The Social Atelier · Draft identity & website concept.",
                    class_name="text-[10px] leading-5 text-[var(--muted)]",
                ),
                rx.el.p(
                    "All portfolio projects and testimonials are fictional demos.",
                    class_name="text-[10px] leading-5 text-[var(--muted)]",
                ),
                rx.el.a(
                    "Back to top",
                    rx.icon("arrow-up", class_name="h-3 w-3"),
                    href="/#home",
                    class_name="flex min-h-11 items-center gap-2 text-[10px] text-[var(--ink)]",
                ),
                class_name="mt-12 flex flex-col gap-2 border-t border-[var(--line)] pt-6 sm:flex-row sm:flex-wrap sm:items-center sm:justify-between",
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 py-12 sm:px-6 lg:px-10 lg:py-16",
        ),
        class_name="w-full bg-[var(--paper)]",
    )
