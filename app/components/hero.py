import reflex as rx

from app.content import BUSINESS


VALUE_POINTS: list[str] = [
    "Strategy before posting",
    "Creative with intention",
    "Consistency, not shortcuts",
]


def phone_mockup() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute left-[12%] top-[12%] h-[70%] w-[76%] rounded-[48%_52%_62%_38%] bg-[var(--surface)]",
            aria_hidden="true",
        ),
        rx.el.div(
            class_name="hero-arc absolute left-[4%] top-[7%] h-[82%] w-[88%] rounded-full border border-[#B79245]/50",
            aria_hidden="true",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("camera", class_name="h-5 w-5"),
                class_name="floating-mark absolute left-[6%] top-[22%] flex h-12 w-12 items-center justify-center rounded-xl border border-[var(--line)] bg-[var(--paper)] text-[var(--ink)]",
            ),
            rx.el.div(
                rx.icon("contact", class_name="h-5 w-5"),
                class_name="floating-mark-delayed absolute right-[6%] top-[12%] flex h-12 w-12 items-center justify-center rounded-full border border-[var(--line)] bg-[var(--paper)] text-[var(--ink)]",
            ),
            rx.el.div(
                rx.icon("play", class_name="h-5 w-5"),
                class_name="floating-mark absolute bottom-[18%] right-[5%] flex h-12 w-12 items-center justify-center rounded-xl border border-[var(--line)] bg-[var(--paper)] text-[var(--ink)]",
            ),
            aria_hidden="true",
        ),
        rx.el.div(
            rx.el.div(
                class_name="mx-auto mb-4 h-2 w-16 rounded-full bg-[#153B2B]"
            ),
            rx.el.div(
                rx.el.span(
                    "the.daily.edit", class_name="text-[10px] font-semibold"
                ),
                rx.icon("ellipsis", class_name="h-4 w-4"),
                class_name="flex items-center justify-between border-b border-[#D9CFBB] pb-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("sprout", class_name="h-5 w-5"),
                    class_name="flex h-8 w-8 items-center justify-center rounded-full bg-[#EEE5D3]",
                ),
                rx.el.div(
                    rx.el.p(
                        "A little more intention.",
                        class_name="text-[10px] font-semibold",
                    ),
                    rx.el.p(
                        "Concept feed · Editorial study",
                        class_name="mt-1 text-[8px] text-[#4E5C4D]",
                    ),
                ),
                class_name="flex items-center gap-2 py-3",
            ),
            rx.el.div(
                rx.el.span(
                    "THE SLOW EDIT", class_name="text-[8px] tracking-[0.2em]"
                ),
                rx.el.div(
                    rx.icon(
                        "flower-2",
                        class_name="h-16 w-16 stroke-[1] text-[#D7BE82]",
                    ),
                    class_name="my-5 flex justify-center",
                ),
                rx.el.p(
                    "Good things",
                    class_name="font-['Playfair_Display'] text-2xl",
                ),
                rx.el.p(
                    "take intention.",
                    class_name="font-['Playfair_Display'] text-2xl italic",
                ),
                rx.el.span(
                    "A FICTIONAL BRAND CONCEPT",
                    class_name="mt-5 block text-[7px] tracking-[0.12em] text-[#D7BE82]",
                ),
                class_name="rounded-t-[70px] bg-[#153B2B] px-4 py-6 text-center text-[#F7F2E7]",
            ),
            rx.el.div(
                rx.icon("heart", class_name="h-4 w-4"),
                rx.icon("message-circle", class_name="h-4 w-4"),
                rx.icon("send", class_name="h-4 w-4"),
                rx.icon("bookmark", class_name="ml-auto h-4 w-4"),
                class_name="flex gap-3 py-3",
            ),
            rx.el.p(
                "A considered story, one post at a time.",
                class_name="text-[9px] leading-relaxed",
            ),
            rx.el.div(
                rx.icon("house", class_name="h-4 w-4"),
                rx.icon("search", class_name="h-4 w-4"),
                rx.icon("circle-plus", class_name="h-4 w-4"),
                rx.icon("clapperboard", class_name="h-4 w-4"),
                rx.icon("user", class_name="h-4 w-4"),
                class_name="mt-4 flex justify-between border-t border-[#D9CFBB] pt-3",
            ),
            class_name="relative z-10 mx-auto w-[208px] rotate-[-6deg] rounded-[32px] border-[7px] border-[#17231D] bg-[#F7F2E7] px-3 pb-4 pt-3 text-[#17231D] sm:w-[232px]",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("calendar-check", class_name="h-4 w-4 text-[#153B2B]"),
                rx.el.span(
                    "A planned presence",
                    class_name="text-[10px] font-semibold text-[#17231D]",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.p(
                "12 / 12",
                class_name="mt-2 text-2xl font-semibold tracking-tight text-[#153B2B]",
            ),
            rx.el.p(
                "Illustrative scheduled posts",
                class_name="text-[9px] text-[#4E5C4D]",
            ),
            class_name="floating-mark-delayed absolute bottom-[14%] left-[1%] z-20 rounded-xl border border-[#D9CFBB] bg-[#F7F2E7] p-3 sm:left-[4%] sm:p-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "chart-no-axes-combined",
                    class_name="h-4 w-4 text-[#153B2B]",
                ),
                rx.el.span(
                    "Sample insights",
                    class_name="text-[10px] font-semibold text-[#17231D]",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.div(class_name="h-4 w-3 rounded-t-sm bg-[#D7BE82]"),
                rx.el.div(class_name="h-7 w-3 rounded-t-sm bg-[#B79245]"),
                rx.el.div(class_name="h-5 w-3 rounded-t-sm bg-[#D7BE82]"),
                rx.el.div(class_name="h-9 w-3 rounded-t-sm bg-[#153B2B]"),
                rx.el.div(class_name="h-8 w-3 rounded-t-sm bg-[#B79245]"),
                class_name="my-2 flex h-10 items-end gap-2",
            ),
            rx.el.p(
                "Illustration, not campaign results",
                class_name="text-[8px] text-[#4E5C4D]",
            ),
            class_name="floating-mark absolute right-0 top-[43%] z-20 rounded-xl border border-[#D9CFBB] bg-[#F7F2E7] p-3 sm:right-[2%]",
        ),
        role="img",
        aria_label="Illustrative social feed phone mockup with fictional content and sample metrics, not real campaign performance.",
        class_name="relative mx-auto flex min-h-[480px] w-full max-w-[470px] items-center justify-center py-9 sm:min-h-[530px]",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    rx.el.span(
                        class_name="h-1.5 w-1.5 rounded-full bg-[#B79245]"
                    ),
                    "SOCIAL MEDIA, WITH INTENTION",
                    class_name="mb-6 flex items-center gap-3 text-[10px] font-semibold tracking-[0.2em] text-[var(--muted)]",
                ),
                rx.el.h1(
                    "A social presence",
                    rx.el.br(),
                    "that feels ",
                    rx.el.em(
                        "like you.",
                        class_name="font-['Playfair_Display'] font-normal text-[var(--display)]",
                    ),
                    class_name="text-[clamp(2.5rem,5.2vw,4.65rem)] font-medium leading-[1.12] tracking-[-0.055em] text-[var(--ink)]",
                ),
                rx.el.p(
                    BUSINESS["tagline"],
                    class_name="mt-7 text-lg font-medium text-[var(--ink)]",
                ),
                rx.el.p(
                    "Strategy, creative content and consistent brand presence. We bring the plan, the craft and the care — so you can focus on the business behind the brand.",
                    class_name="mt-3 max-w-lg text-sm leading-7 text-[var(--muted)] sm:text-base",
                ),
                rx.el.div(
                    rx.el.a(
                        "Let’s build your presence",
                        rx.icon("arrow-up-right", class_name="h-4 w-4"),
                        href="#contact",
                        class_name="flex min-h-12 items-center justify-center gap-3 rounded-full bg-[var(--primary)] px-6 py-3 text-sm font-medium text-[var(--on-primary)] transition-opacity hover:opacity-85",
                    ),
                    rx.el.a(
                        rx.icon("play", class_name="h-4 w-4"),
                        "Explore our work",
                        href="#work",
                        class_name="flex min-h-12 items-center justify-center gap-3 rounded-full border border-[var(--line)] px-6 py-3 text-sm font-medium text-[var(--ink)] transition-colors hover:bg-[var(--surface)]",
                    ),
                    class_name="mt-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap",
                ),
                rx.el.ul(
                    rx.foreach(
                        VALUE_POINTS,
                        lambda point: rx.el.li(
                            rx.icon(
                                "check",
                                class_name="h-3.5 w-3.5 shrink-0 text-[var(--display)]",
                            ),
                            point,
                            class_name="flex items-center gap-2 text-[10px] text-[var(--muted)] sm:text-[11px]",
                            key=point,
                        ),
                    ),
                    class_name="mt-7 flex flex-wrap gap-x-5 gap-y-3",
                ),
                class_name="hero-enter min-w-0 py-8 lg:py-12",
            ),
            rx.el.div(
                phone_mockup(),
                rx.el.p(
                    "DESIGN STUDY · ALL CONTENT & METRICS ARE ILLUSTRATIVE",
                    class_name="text-center text-[8px] tracking-[0.1em] text-[var(--muted)]",
                ),
                class_name="hero-enter-late min-w-0",
            ),
            class_name="mx-auto grid w-full max-w-[1280px] items-center gap-4 px-5 py-8 sm:px-6 lg:grid-cols-[1.1fr_1fr] lg:gap-8 lg:px-10 lg:py-14",
        ),
        id="home",
        class_name="relative w-full border-b border-[var(--line)] bg-[var(--paper)]",
    )
