import reflex as rx

from app.components.navigation import navigation
from app.components.home_sections import footer
from app.components.contact import floating_contact
from app.states.home_state import HomeState
from app.content import LEGAL_LINKS


PRIVACY: list[tuple[str, str]] = [
    (
        "Status and responsible business",
        "This is a draft privacy notice for The Social Atelier, a temporary agency identity. The legal business name, registered address, privacy contact and applicable jurisdiction remain unverified. This notice describes the current enquiry experience, not a completed compliance assessment. Do not submit sensitive information while the operator is unverified.",
    ),
    (
        "Information you provide",
        "The general contact form collects your name, phone, email, business name, subject and message. The custom-plan form also collects your selected platforms, services, content needs, budget and other details you enter. These enquiries are saved for review. You do not need to provide passwords, payment-card details, identity documents, health information or confidential client data; do not include them.",
    ),
    (
        "Why information is used",
        "Enquiry information is intended to help understand your requirements, prepare a possible quotation and respond using your contact details. Sending an enquiry is not a purchase or agreement to marketing. No marketing subscription is created by the contact form. The owner must confirm who can access enquiries and the lawful basis for each use before live operations.",
    ),
    (
        "Storage, access and retention",
        "Submitted enquiries are stored by this website. Hosting providers and authorized operators may need access to support the service. A specific retention period, access process, backup arrangements and deletion procedure have not yet been approved. No fixed deletion deadline or guarantee of security is asserted. The owner must establish a documented retention schedule and appropriate safeguards before business launch.",
    ),
    (
        "Browser storage and external resources",
        "A theme preference is stored locally in your browser so light or dark mode can be remembered. The interactive website uses a session connection to process form events. Fonts are loaded from Google Fonts, which may receive technical request information such as your IP address. No advertising or analytics tracking is intentionally added by this site’s current implementation; the owner must verify the full hosting setup before making a broader cookie claim. Clearing site data removes the saved theme preference.",
    ),
    (
        "Payments and third-party sites",
        "Payments remain on hold pending commercial approval and payment setup. If enabled later, Razorpay will handle payment details under its own policies; this website’s checkout is designed not to collect card information. Payment-related order and verification records may be stored. Verified external contact or social links take you to separate services with their own privacy practices. Placeholder channels are not clickable.",
    ),
    (
        "Your requests and choices",
        "You may use the contact form to ask about access, correction, deletion or use of your enquiry details. Select a clear subject such as ‘Privacy request’ and provide only the information needed to identify your enquiry; do not send identity documents here. This saves a request, but the responsible operator and response process are still pending verification. Applicable rights and deadlines depend on law and are not waived by this draft.",
    ),
    (
        "Children, transfers and updates",
        "This draft service is intended for business enquiries and does not invite children to submit personal data. Hosting location, international transfers and any required protections must be verified by the owner. Material changes should be reflected in an approved, dated notice before launch. There is no claimed legal effective date for this draft.",
    ),
]
TERMS: list[tuple[str, str]] = [
    (
        "Draft status; no live offer",
        "The Social Atelier is a temporary identity, not a verified legal contracting party. This website illustrates a proposed social media service. These draft terms do not create a service contract or replace applicable law. The owner must verify the business, jurisdiction and final terms before accepting orders. Payments are currently on hold.",
    ),
    (
        "Enquiries and scope",
        "Submitting either enquiry form records a request for discussion or quotation, not an order, reservation, accepted proposal or guaranteed response. Before any engagement, the parties should agree in writing on the verified supplier, selected platforms, deliverables, asset counts, duration, responsibilities, approval process, fees and commercial policies.",
    ),
    (
        "Prices, taxes and exclusions",
        "Displayed INR prices are editable draft totals for the entire chosen duration, not monthly instalments. No tax rate or invoicing treatment is assumed. Advertising spend, creator fees, on-location shoots, travel, paid tools and third-party licences are excluded unless expressly included in the final written scope. Final pricing, taxes and payment schedule require owner approval. A highlighted plan is an editorial selection, not proof of sales popularity.",
    ),
    (
        "Client materials and authorized access",
        "A future engagement should identify who supplies brand assets, accurate business information and licensed footage, and who holds rights to use them. Do not send passwords in forms. Any account access should use the platform’s authorized roles and permissions. Content ownership, licence scope, handover files and portfolio permissions need explicit written agreement; no transfer is promised by this draft.",
    ),
    (
        "Approvals, revisions and timelines",
        "The proposed process includes planning, creative review and approval before publication. Final agreements must specify revision limits, review windows, publishing responsibilities, working hours, escalation arrangements and the treatment of delays or scope changes. No delivery date or service availability is established merely by submitting an enquiry.",
    ),
    (
        "Results and platform dependencies",
        "Follower growth, reach, leads, sales and viral performance are not guaranteed. Results depend on many factors outside a creative team’s control. Platform availability, permissions and rules can change. Reports should use available metrics with context. No fabricated reviews, misleading claims or unauthorized content should be requested.",
    ),
    (
        "Payments, cancellation and disputes",
        "Checkout may only proceed once the owner approves commercial terms and configures the payment service. A browser payment callback is not proof of a completed order; confirmation requires verification. The separate Refund / Cancellation draft identifies matters that must be agreed before payment. Dispute process, governing law and liability provisions require qualified review; no jurisdiction, penalty or exclusion of statutory rights is invented here.",
    ),
    (
        "Website content and acceptable use",
        "Portfolio projects and testimonials are fictional, labelled demos, not customer endorsements or measured results. Contact and social channels are placeholders until verified. Use forms for legitimate enquiries; do not submit unlawful content, impersonate others, send sensitive credentials or abuse the service. The general enquiry form suppresses repeat identical submissions over a short interval.",
    ),
    (
        "Questions and future approval",
        "Ask a terms or scope question through the contact form. Direct business channels are unavailable until verified, and no response deadline is promised. Before launch, these drafts must be replaced or explicitly approved with the real contracting party, contact information, policy dates and any required disclosures. Later changes should be communicated before they apply to an agreed engagement.",
    ),
]
REFUNDS: list[tuple[str, str]] = [
    (
        "Draft policy; payment hold",
        "This is a planning document, not an approved refund promise or a blanket ‘no refunds’ rule. The business identity and commercial policies remain pending verification, and payments are on hold. No refund percentage, deadline, cancellation fee or automatic renewal is assumed. Applicable statutory rights are not displaced by this draft.",
    ),
    (
        "Cancelling an enquiry",
        "Contact and custom-plan submissions are enquiries only. There is no service purchase to cancel simply because you submitted a form. To withdraw interest or request deletion of enquiry information, send a contact-form message with an appropriate subject. The request can be saved; the operator’s review availability is not yet verified.",
    ),
    (
        "Before a future paid engagement",
        "Before accepting money, the owner must publish approved rules covering cancellation before work starts, completed versus uncompleted work, committed third-party costs, prepaid multi-month terms, pause requests, rescheduling and termination. The written scope should explain what happens to unused services and deliverables. Do not assume a draft duration price establishes any of these rules.",
    ),
    (
        "How to raise a cancellation or refund request",
        "Use the contact form with the subject ‘Cancellation request’ or ‘Refund request’. Include your name, business, the relevant order reference if one exists, a brief reason and a way to reach you. Never include card numbers, passwords, OTPs or payment signatures. A saved request is not approval of a refund or confirmation of cancellation; eligibility and next steps require the verified operator’s review.",
    ),
    (
        "Failed, duplicate or unclear payments",
        "If a future checkout reports an uncertain payment, check the payment status and your bank record before retrying. Do not assume a debit is a confirmed captured payment or that it automatically entitles you to a service. For an apparent duplicate charge or failed debit, retain your payment reference and ask the operator or payment provider to investigate. Bank and provider timelines vary; none is promised here.",
    ),
    (
        "Review and processing",
        "Approved policies must specify how requests are acknowledged, which records are needed, who decides eligibility, how an approved refund is initiated and how the customer is notified. Processor or banking delays should be distinguished from the business’s decision. This draft does not establish processing times, an alternate payout method or a guaranteed outcome.",
    ),
    (
        "Scope changes and third-party commitments",
        "Service changes, missed approvals, platform restrictions and already committed production or media costs should be dealt with in a written agreement before payment. Whether any cost is deductible depends on approved terms and applicable law; this draft authorizes no automatic deductions. Advertising budgets and creator fees are separately scoped.",
    ),
    (
        "Approval and contact details",
        "The owner must verify the legal business identity, support channels, applicable consumer obligations and final policy before taking payment. Until then, the contact form can save questions, but direct phone, email and WhatsApp placeholders are not service channels. No legal effective date or binding refund schedule is claimed.",
    ),
]


def legal_page(
    title: str, introduction: str, sections: list[tuple[str, str]]
) -> rx.Component:
    return rx.el.div(
        navigation(),
        rx.el.main(
            rx.el.a(
                "Back to the atelier",
                rx.icon("arrow-left", class_name="h-4 w-4"),
                href="/",
                class_name="inline-flex min-h-11 items-center gap-2 text-sm text-[var(--muted)]",
            ),
            rx.el.p(
                "DRAFT · PENDING BUSINESS VERIFICATION",
                class_name="mt-6 text-xs font-semibold tracking-wider text-[var(--display)]",
            ),
            rx.el.h1(
                title,
                class_name="mt-5 font-['Playfair_Display'] text-3xl leading-tight text-[var(--ink)] sm:text-5xl",
            ),
            rx.el.p(
                introduction,
                class_name="mt-6 text-base leading-8 text-[var(--muted)]",
            ),
            rx.el.nav(
                rx.foreach(
                    LEGAL_LINKS,
                    lambda link: rx.el.a(
                        link[0],
                        href=link[1],
                        class_name="min-h-11 py-3 text-xs text-[var(--ink)] underline underline-offset-4",
                    ),
                ),
                aria_label="Legal policies",
                class_name="mt-8 flex flex-wrap gap-x-6 border-y border-[var(--line)] py-3",
            ),
            rx.foreach(
                sections,
                lambda section: rx.el.section(
                    rx.el.h2(
                        section[0],
                        class_name="text-xl font-semibold text-[var(--ink)]",
                    ),
                    rx.el.p(
                        section[1],
                        class_name="mt-4 text-sm leading-8 text-[var(--muted)]",
                    ),
                    class_name="border-b border-[var(--line)] py-8",
                ),
            ),
            rx.el.a(
                "Ask a question about this policy",
                href="/#contact",
                class_name="mt-8 inline-flex min-h-12 items-center rounded-full bg-[var(--primary)] px-6 py-3 text-sm text-[var(--on-primary)]",
            ),
            id="main-content",
            tab_index=-1,
            class_name="mx-auto w-full min-w-0 max-w-4xl px-5 py-12 sm:px-8 sm:py-16",
        ),
        footer(),
        floating_contact(),
        custom_attrs={"data-theme": HomeState.theme},
        class_name="atelier min-h-dvh w-full min-w-0 overflow-x-clip bg-[var(--paper)] font-['Inter'] text-[var(--ink)]",
    )


def privacy_page() -> rx.Component:
    return legal_page(
        "Privacy Policy",
        "What the enquiry forms collect, how they are intended to be used, and what still needs owner verification.",
        PRIVACY,
    )


def terms_page() -> rx.Component:
    return legal_page(
        "Terms & Conditions",
        "Understand the draft service scope, enquiry status and matters that must be agreed before a paid engagement.",
        TERMS,
    )


def refunds_page() -> rx.Component:
    return legal_page(
        "Refund / Cancellation Policy",
        "A transparent draft guide to cancellation questions and future payment review — without invented refund promises.",
        REFUNDS,
    )
