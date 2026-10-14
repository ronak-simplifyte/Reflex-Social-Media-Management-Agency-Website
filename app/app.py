import reflex as rx

from app import models
from app.components.navigation import navigation
from app.components.hero import hero
from app.components.home_sections import (
    platforms,
    problems_solution,
    services,
    process,
    portfolio,
    industries,
    benefits_about,
    comparison,
    testimonials,
    faqs,
    contact_cta,
    footer,
)
from app.states.home_state import HomeState
from app.states.checkout_state import CheckoutState
from app.components.pricing import pricing
from app.components.checkout import checkout_page
from app.components.contact import contact_section, floating_contact
from app.pages.legal import privacy_page, terms_page, refunds_page

__all__ = ["app", "index", "models"]


def index() -> rx.Component:
    return rx.el.div(
        navigation(),
        rx.el.main(
            hero(),
            platforms(),
            problems_solution(),
            services(),
            process(),
            portfolio(),
            industries(),
            benefits_about(),
            comparison(),
            testimonials(),
            pricing(),
            faqs(),
            contact_cta(),
            contact_section(),
            id="main-content",
            tab_index=-1,
            class_name="min-w-0 w-full",
        ),
        footer(),
        floating_contact(),
        custom_attrs={"data-theme": HomeState.theme},
        class_name="atelier min-h-dvh min-w-0 w-full overflow-x-clip bg-[var(--paper)] font-['Inter'] text-[var(--ink)]",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/atelier.css"],
    head_components=[
        rx.el.link(rel="icon", href="/favicon.ico", type="image/x-icon"),
        rx.el.meta(name="theme-color", content="#153B2B"),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap",
            rel="stylesheet",
        ),
    ],
)


def page_meta(
    title: str, description: str, private: bool = False
) -> list[dict[str, str]]:
    metadata = [
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:type", "content": "website"},
        {"name": "twitter:card", "content": "summary"},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
    ]
    if private:
        metadata.append({"name": "robots", "content": "noindex, nofollow"})
    return metadata


HOME_TITLE = "The Social Atelier | Thoughtful Social Media — Draft Agency"
HOME_DESCRIPTION = "Explore draft social media strategy, creative and management plans. View clearly labelled concepts and send an enquiry; business verification and payments are pending."
PRIVACY_TITLE = "Privacy Policy | The Social Atelier"
PRIVACY_DESCRIPTION = "Draft privacy notice: enquiry data, intended uses, browser storage, external services and privacy requests pending business verification."
TERMS_TITLE = "Terms & Conditions | The Social Atelier"
TERMS_DESCRIPTION = "Draft service terms covering enquiries, scope, prices, approvals and responsibilities. Commercial approval and business verification are pending."
REFUNDS_TITLE = "Refund / Cancellation Policy | The Social Atelier"
REFUNDS_DESCRIPTION = "Draft guidance for withdrawing enquiries, cancellation questions and payment review. Payments remain on hold; no refund timeline or entitlement is invented."
CHECKOUT_TITLE = "Checkout on Hold | The Social Atelier"
CHECKOUT_DESCRIPTION = "Review your selected draft plan. Payment remains on hold until the owner verifies business terms and configures the payment service."

app.add_page(
    index,
    route="/",
    title=HOME_TITLE,
    description=HOME_DESCRIPTION,
    image="",
    meta=page_meta(HOME_TITLE, HOME_DESCRIPTION),
)
app.add_page(
    privacy_page,
    route="/privacy-policy",
    title=PRIVACY_TITLE,
    description=PRIVACY_DESCRIPTION,
    image="",
    meta=page_meta(PRIVACY_TITLE, PRIVACY_DESCRIPTION),
)
app.add_page(
    terms_page,
    route="/terms-and-conditions",
    title=TERMS_TITLE,
    description=TERMS_DESCRIPTION,
    image="",
    meta=page_meta(TERMS_TITLE, TERMS_DESCRIPTION),
)
app.add_page(
    refunds_page,
    route="/refund-cancellation-policy",
    title=REFUNDS_TITLE,
    description=REFUNDS_DESCRIPTION,
    image="",
    meta=page_meta(REFUNDS_TITLE, REFUNDS_DESCRIPTION),
)
app.add_page(
    checkout_page,
    route="/checkout",
    on_load=CheckoutState.load_checkout,
    title=CHECKOUT_TITLE,
    description=CHECKOUT_DESCRIPTION,
    image="",
    meta=page_meta(CHECKOUT_TITLE, CHECKOUT_DESCRIPTION, private=True),
)
