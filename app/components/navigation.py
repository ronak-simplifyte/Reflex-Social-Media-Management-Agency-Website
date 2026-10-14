import reflex as rx

from app.content import BUSINESS
from app.states.home_state import HomeState


NAVIGATION: list[dict[str, str]] = [
    {"label": "Home", "href": "/#home"},
    {"label": "Services", "href": "/#services"},
    {"label": "Plans", "href": "/#plans"},
    {"label": "Our Work", "href": "/#work"},
    {"label": "How It Works", "href": "/#process"},
    {"label": "About", "href": "/#about"},
    {"label": "Contact", "href": "/#contact"},
]


def brand() -> rx.Component:
    return rx.el.a(
        rx.el.span(
            rx.icon(BUSINESS["logo_icon"], class_name="h-6 w-6"),
            class_name="flex h-10 w-10 shrink-0 items-center justify-center rounded-full border border-[var(--line)] text-[var(--ink)]",
        ),
        rx.el.span(
            rx.el.span(
                BUSINESS["name"].removesuffix(" (placeholder)"),
                class_name="block text-sm font-semibold tracking-tight sm:text-base",
            ),
            rx.el.span(
                "DRAFT AGENCY IDENTITY",
                class_name="block text-[8px] tracking-[0.18em] text-[var(--muted)]",
            ),
            class_name="min-w-0",
        ),
        href="/#home",
        aria_label="The Social Atelier, home — draft agency identity",
        class_name="flex min-w-0 items-center gap-2 text-[var(--ink)] sm:gap-3",
    )


def theme_toggle() -> rx.Component:
    return rx.el.button(
        rx.cond(
            HomeState.theme == "dark",
            rx.icon("sun", class_name="h-4 w-4"),
            rx.icon("moon", class_name="h-4 w-4"),
        ),
        on_click=HomeState.toggle_theme,
        type="button",
        aria_label=rx.cond(
            HomeState.theme == "dark",
            "Switch to light theme",
            "Switch to dark theme",
        ),
        class_name="flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-[var(--line)] bg-transparent text-[var(--ink)] transition-colors hover:bg-[var(--surface)]",
    )


def mobile_menu() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(
            rx.el.button(
                rx.icon("menu", class_name="h-5 w-5"),
                type="button",
                aria_label="Open navigation menu",
                class_name="flex h-11 w-11 items-center justify-center rounded-full border border-[var(--line)] bg-transparent text-[var(--ink)]",
            ),
            as_child=True,
        ),
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 z-50 bg-black/50"
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.radix.primitives.dialog.title(
                        "Explore the atelier",
                        class_name="text-lg font-semibold text-[var(--ink)]",
                    ),
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            rx.icon("x", class_name="h-5 w-5"),
                            type="button",
                            aria_label="Close navigation menu",
                            class_name="flex h-11 w-11 items-center justify-center rounded-full border border-[var(--line)] text-[var(--ink)]",
                        ),
                        as_child=True,
                    ),
                    class_name="flex items-center justify-between gap-3",
                ),
                rx.radix.primitives.dialog.description(
                    "Thoughtful social. Meaningful presence.",
                    class_name="mt-3 text-sm text-[var(--muted)]",
                ),
                rx.el.nav(
                    rx.foreach(
                        NAVIGATION,
                        lambda item: rx.radix.primitives.dialog.close(
                            rx.el.a(
                                item["label"],
                                rx.icon("arrow-up-right", class_name="h-4 w-4"),
                                href=item["href"],
                                class_name="flex min-h-12 items-center justify-between border-b border-[var(--line)] py-3 text-lg text-[var(--ink)]",
                                key=item["href"],
                            ),
                            as_child=True,
                        ),
                    ),
                    aria_label="Mobile navigation",
                    class_name="mt-6 flex flex-col",
                ),
                rx.radix.primitives.dialog.close(
                    rx.el.a(
                        "Get started",
                        rx.icon("arrow-right", class_name="h-4 w-4"),
                        href="/#contact",
                        class_name="mt-8 flex min-h-12 items-center justify-center gap-3 rounded-full bg-[var(--primary)] px-6 py-3 font-medium text-[var(--on-primary)]",
                    ),
                    as_child=True,
                ),
                class_name="mobile-drawer fixed inset-y-0 right-0 z-[60] w-[min(90vw,380px)] overflow-y-auto border-l border-[var(--line)] bg-[var(--paper)] p-6 text-[var(--ink)] outline-hidden",
            ),
        ),
    )


def navigation() -> rx.Component:
    return rx.el.header(
        rx.el.a(
            "Skip to content",
            href="#main-content",
            class_name="sr-only z-[80] rounded-full bg-[var(--primary)] p-4 text-[var(--on-primary)] focus:not-sr-only focus:fixed focus:left-4 focus:top-4",
        ),
        rx.el.div(
            brand(),
            rx.el.nav(
                rx.foreach(
                    NAVIGATION,
                    lambda item: rx.el.a(
                        item["label"],
                        href=item["href"],
                        key=item["href"],
                        class_name="flex min-h-11 items-center text-xs font-medium text-[var(--muted)] transition-colors hover:text-[var(--ink)]",
                    ),
                ),
                aria_label="Main navigation",
                class_name="hidden items-center gap-5 xl:flex",
            ),
            rx.el.div(
                theme_toggle(),
                rx.el.a(
                    "Get started",
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    href="/#contact",
                    class_name="hidden min-h-11 items-center gap-3 rounded-full bg-[var(--primary)] px-5 text-xs font-semibold text-[var(--on-primary)] transition-opacity hover:opacity-85 sm:flex",
                ),
                rx.el.div(mobile_menu(), class_name="xl:hidden"),
                class_name="flex shrink-0 items-center gap-2",
            ),
            class_name="mx-auto flex min-h-20 w-full max-w-[1280px] items-center justify-between gap-3 px-4 sm:px-6 lg:px-10",
        ),
        class_name="sticky top-0 z-40 w-full border-b border-[var(--line)] bg-[var(--paper)] text-[var(--ink)]",
    )
