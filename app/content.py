"""Editable website content; importing this module performs no I/O.

This is draft configuration, not live business information or approved pricing.
Edit the constants below; stable IDs can later become admin-managed record keys.
Blank savings labels hide the optional label. Prices are integer INR totals for
an entire duration, not monthly instalments; future checkout must price on the
backend and convert approved totals to paise. Checkout is held until the owner
sets approved_for_checkout after confirming commercial terms.
Contact/social URLs are reserved example.com placeholders and must not be made
clickable until replaced and enabled. All case studies and quotations are demos.
"""

import reflex as rx

from typing import Literal, TypedDict
from urllib.parse import urlparse


class PlaceholderLink(TypedDict):
    label: str
    value: str
    url: str
    is_placeholder: bool
    enabled: bool
    notice: str


class BusinessContent(TypedDict):
    name: str
    name_is_placeholder: bool
    logo_mark: str
    logo_icon: str
    logo_is_placeholder: bool
    tagline: str
    description: str
    placeholder_notice: str
    address: str
    address_is_placeholder: bool
    contact_links: dict[str, PlaceholderLink]
    social_links: dict[str, PlaceholderLink]


class ThemePalette(TypedDict):
    background: str
    surface: str
    foreground: str
    muted_foreground: str
    primary: str
    primary_foreground: str
    accent: str
    accent_soft: str
    border: str


class DesignContent(TypedDict):
    direction: str
    body_font: str
    display_font: str
    display_font_usage: str
    default_theme: str
    light: ThemePalette
    dark: ThemePalette
    spacing: dict[str, str]
    principles: list[str]


class PlatformContent(TypedDict):
    id: str
    name: str
    icon: str
    description: str
    formats: list[str]


class ServiceContent(TypedDict):
    id: str
    title: str
    description: str


class ServiceCategory(TypedDict):
    id: str
    title: str
    icon: str
    description: str
    services: list[ServiceContent]


class EditorialItem(TypedDict):
    id: str
    title: str
    description: str
    icon: str


class PortfolioContent(TypedDict):
    id: str
    title: str
    industry: str
    platforms: list[str]
    services: list[str]
    brief: str
    approach: str
    deliverables: list[str]
    image_url: str
    image_alt: str
    is_demo: bool
    demo_label: str
    disclaimer: str


class IndustryContent(TypedDict):
    id: str
    label: str
    icon: str


class ComparisonContent(TypedDict):
    id: str
    topic: str
    before: str
    after: str


class TestimonialContent(TypedDict):
    id: str
    quote: str
    attribution: str
    role: str
    is_demo: bool
    demo_label: str
    disclaimer: str


class FAQContent(TypedDict):
    id: str
    question: str
    answer: str


DurationId = Literal["monthly", "six_months", "one_year"]
PlanId = Literal["basic", "standard", "premium"]


class DurationContent(TypedDict):
    id: DurationId
    label: str
    months: int


class PriceContent(TypedDict):
    total_inr: int
    savings_label: str


class PlanContent(TypedDict):
    id: PlanId
    name: str
    description: str
    highlighted: bool
    highlight_label: str
    features: list[str]
    prices: dict[DurationId, PriceContent]


class PricingContent(TypedDict):
    currency: str
    price_basis: str
    default_duration_id: DurationId
    default_plan_id: PlanId
    is_draft: bool
    approved_for_checkout: bool
    notice: str
    tax_notice: str
    exclusions: list[str]
    custom_plan_title: str
    custom_plan_description: str
    durations: list[DurationContent]
    plans: list[PlanContent]


BUSINESS: BusinessContent = {
    "name": "The Social Atelier (placeholder)",
    "name_is_placeholder": True,
    "logo_mark": "SA",
    "logo_icon": "sprout",
    "logo_is_placeholder": True,
    "tagline": "Thoughtful social. Meaningful presence.",
    "description": "A draft social media agency identity focused on strategy, creative content and consistent brand presence.",
    "placeholder_notice": "Temporary business identity. All contact details, addresses and social links are placeholders; no real agency affiliation is implied.",
    "address": "Office address pending business verification (placeholder)",
    "address_is_placeholder": True,
    "contact_links": {
        "phone": {
            "label": "Phone",
            "value": "Business number pending verification (placeholder)",
            "url": "https://example.com/placeholder/phone",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Replace with a verified business number and tel: URL before publishing.",
        },
        "whatsapp": {
            "label": "WhatsApp",
            "value": "+91 00000 00000 (placeholder)",
            "url": "https://example.com/placeholder/whatsapp",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Replace with a verified business WhatsApp number and wa.me URL before publishing.",
        },
        "email": {
            "label": "Email",
            "value": "Business mailbox pending verification (placeholder)",
            "url": "https://example.com/placeholder/email",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Replace with a verified business mailbox and mailto: URL before publishing.",
        },
        "address": {
            "label": "Visit us",
            "value": "Office location to be confirmed (placeholder)",
            "url": "https://example.com/placeholder/location",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Replace with a verified business address and map URL before publishing.",
        },
    },
    "social_links": {
        "instagram": {
            "label": "Instagram",
            "value": "Profile to be confirmed",
            "url": "https://example.com/placeholder/instagram",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Placeholder URL, not an agency profile.",
        },
        "facebook": {
            "label": "Facebook",
            "value": "Page to be confirmed",
            "url": "https://example.com/placeholder/facebook",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Placeholder URL, not an agency page.",
        },
        "linkedin": {
            "label": "LinkedIn",
            "value": "Company page to be confirmed",
            "url": "https://example.com/placeholder/linkedin",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Placeholder URL, not an agency page.",
        },
        "youtube": {
            "label": "YouTube",
            "value": "Channel to be confirmed",
            "url": "https://example.com/placeholder/youtube",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Placeholder URL, not an agency channel.",
        },
        "x": {
            "label": "X",
            "value": "Profile to be confirmed",
            "url": "https://example.com/placeholder/x",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Placeholder URL, not an agency profile.",
        },
        "pinterest": {
            "label": "Pinterest",
            "value": "Profile to be confirmed",
            "url": "https://example.com/placeholder/pinterest",
            "is_placeholder": True,
            "enabled": False,
            "notice": "Placeholder URL, not an agency profile.",
        },
    },
}


def verified_link(link: PlaceholderLink) -> bool:
    parsed = urlparse(link["url"])
    host = (parsed.hostname or "").lower()
    if (
        not link["enabled"]
        or link["is_placeholder"]
        or not link["value"].strip()
    ):
        return False
    if (
        "placeholder" in link["url"].lower()
        or host in ("example.com", "example.org", "example.net", "localhost")
        or host.endswith(".example.com")
    ):
        return False
    if link["label"] == "Phone":
        import re

        return parsed.scheme == "tel" and bool(
            re.fullmatch(r"\+?[0-9 ()-]{7,32}", parsed.path)
        )
    if link["label"] == "Email":
        import re

        return (
            parsed.scheme == "mailto"
            and bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", parsed.path))
            and "example." not in parsed.path
        )
    if link["label"] == "WhatsApp":
        return (
            parsed.scheme == "https"
            and host in ("wa.me", "api.whatsapp.com", "web.whatsapp.com")
            and bool(parsed.path.strip("/") or parsed.query)
        )
    return (
        parsed.scheme == "https"
        and bool(host)
        and not parsed.username
        and not parsed.password
    )


WHATSAPP_VERIFIED: bool = verified_link(BUSINESS["contact_links"]["whatsapp"])
LEGAL_LINKS: list[tuple[str, str]] = [
    ("Privacy Policy", "/privacy-policy"),
    ("Terms & Conditions", "/terms-and-conditions"),
    ("Refund / Cancellation Policy", "/refund-cancellation-policy"),
]


DESIGN: DesignContent = {
    "direction": "Mobile-first editorial; warm cream, forest green and muted gold with generous restrained spacing.",
    "body_font": "Inter",
    "display_font": "Playfair Display",
    "display_font_usage": "Selective hero and section-heading accents only; use Inter for body, forms, navigation and pricing.",
    "default_theme": "light",
    "light": {
        "background": "#F7F2E7",
        "surface": "#EEE5D3",
        "foreground": "#153B2B",
        "muted_foreground": "#4E5C4D",
        "primary": "#153B2B",
        "primary_foreground": "#F7F2E7",
        "accent": "#B79245",
        "accent_soft": "#D7BE82",
        "border": "#D9CFBB",
    },
    "dark": {
        "background": "#0C2A20",
        "surface": "#153B2B",
        "foreground": "#F7F2E7",
        "muted_foreground": "#D8D0BD",
        "primary": "#D7BE82",
        "primary_foreground": "#0C2A20",
        "accent": "#B79245",
        "accent_soft": "#D7BE82",
        "border": "#355547",
    },
    "spacing": {
        "mobile_page_gutter": "1.25rem",
        "desktop_page_gutter": "3rem",
        "mobile_section_gap": "4rem",
        "desktop_section_gap": "6rem",
        "card_padding": "1.5rem",
        "content_max_width": "80rem",
    },
    "principles": [
        "Design for small screens first; expand grids only when readable.",
        "Use intentional dark-theme surface and text pairs, not automatic inversion.",
        "Keep gold decorative; verify contrast before using it for small text.",
        "Use generous whitespace, fine borders and minimal shadows; avoid busy gradients.",
        "Use restrained motion and respect reduced-motion preferences.",
        "Preserve visible keyboard focus, readable line lengths and comfortable touch targets.",
    ],
}

PLATFORMS: list[PlatformContent] = [
    {
        "id": "instagram",
        "name": "Instagram",
        "icon": "instagram",
        "description": "Build a coherent visual presence with storytelling, short-form video and community interaction.",
        "formats": ["Reels", "Carousels", "Stories", "Feed posts"],
    },
    {
        "id": "facebook",
        "name": "Facebook",
        "icon": "facebook",
        "description": "Support a business page with useful content, local discovery and audience conversations.",
        "formats": ["Page posts", "Reels", "Stories", "Campaign creatives"],
    },
    {
        "id": "linkedin",
        "name": "LinkedIn",
        "icon": "linkedin",
        "description": "Develop a professional voice through company updates, expertise and founder-led content.",
        "formats": [
            "Thought-leadership posts",
            "Documents",
            "Company updates",
            "Video",
        ],
    },
    {
        "id": "youtube",
        "name": "YouTube",
        "icon": "youtube",
        "description": "Plan discoverable video content with clear packaging and a sustainable publishing schedule.",
        "formats": [
            "Long-form video",
            "Shorts",
            "Thumbnails",
            "Community posts",
        ],
    },
    {
        "id": "x",
        "name": "X",
        "icon": "message-circle",
        "description": "Share timely perspectives and join relevant conversations with a consistent brand voice.",
        "formats": ["Posts", "Threads", "Visual updates"],
    },
    {
        "id": "pinterest",
        "name": "Pinterest",
        "icon": "pin",
        "description": "Organize evergreen visual ideas to support discovery and visits to useful brand resources.",
        "formats": ["Pins", "Boards", "Product inspiration"],
    },
    {
        "id": "google_business",
        "name": "Google Business Profile",
        "icon": "map-pin",
        "description": "Maintain accurate local business information, timely updates and responsible review responses.",
        "formats": ["Business updates", "Photos", "Offers", "Review responses"],
    },
]

SERVICE_CATEGORIES: list[ServiceCategory] = [
    {
        "id": "strategy",
        "title": "Strategy & brand foundations",
        "icon": "compass",
        "description": "Give every channel a purpose before publishing.",
        "services": [
            {
                "id": "social_audit",
                "title": "Social media audit",
                "description": "Review existing profiles, content consistency and opportunities; document practical next steps.",
            },
            {
                "id": "audience_competitor_research",
                "title": "Audience & competitor research",
                "description": "Explore audience needs and relevant competitors to inform positioning, without copying their work.",
            },
            {
                "id": "social_strategy",
                "title": "Social media strategy",
                "description": "Define channel priorities, content pillars, campaign objectives and meaningful measurement criteria.",
            },
            {
                "id": "brand_voice",
                "title": "Brand voice & visual direction",
                "description": "Create guidance for tone, visual consistency and recognizable social templates.",
            },
            {
                "id": "profile_optimization",
                "title": "Profile setup & optimization",
                "description": "Refine bios, profile imagery, highlights and links using verified business information.",
            },
            {
                "id": "content_calendar",
                "title": "Content calendars",
                "description": "Organize monthly themes, formats and approval dates into a manageable publishing plan.",
            },
        ],
    },
    {
        "id": "creative",
        "title": "Content & creative production",
        "icon": "palette",
        "description": "Turn brand ideas into channel-appropriate creative assets.",
        "services": [
            {
                "id": "static_design",
                "title": "Social post & carousel design",
                "description": "Design static posts, educational carousels and branded templates for agreed channels.",
            },
            {
                "id": "copywriting",
                "title": "Captions & social copywriting",
                "description": "Write accessible captions, hooks and calls to action that match the brand voice.",
            },
            {
                "id": "reels_shorts",
                "title": "Reels & Shorts",
                "description": "Develop concepts, scripts and edits for short-form video using agreed source footage.",
            },
            {
                "id": "stories",
                "title": "Stories & interactive content",
                "description": "Plan story sequences, prompts, polls and launch updates suited to each platform.",
            },
            {
                "id": "video_editing",
                "title": "Video editing & motion graphics",
                "description": "Edit long-form or short-form footage with captions, pacing and simple motion elements.",
            },
            {
                "id": "photography_production",
                "title": "Photography & video shoots",
                "description": "Scope product or brand shoots separately, including location, production resources and usage rights.",
            },
            {
                "id": "youtube_packaging",
                "title": "YouTube thumbnails & channel packaging",
                "description": "Create thumbnails, titles, descriptions and channel artwork that accurately represent the video.",
            },
            {
                "id": "campaign_creative",
                "title": "Campaign & launch creatives",
                "description": "Build coordinated creative assets for product launches, seasonal moments and promotions.",
            },
        ],
    },
    {
        "id": "management",
        "title": "Publishing & community management",
        "icon": "calendar-days",
        "description": "Keep profiles organized and audience communication consistent.",
        "services": [
            {
                "id": "account_management",
                "title": "Social media account management",
                "description": "Coordinate approved content, publishing schedules and day-to-day profile maintenance.",
            },
            {
                "id": "scheduling",
                "title": "Scheduling & publishing",
                "description": "Schedule approved assets at agreed times, subject to platform permissions and availability.",
            },
            {
                "id": "community_management",
                "title": "Community & inbox management",
                "description": "Respond to agreed comment and message categories within defined working hours and escalation rules.",
            },
            {
                "id": "hashtag_discovery",
                "title": "Hashtag & discoverability research",
                "description": "Research relevant keywords, tags and metadata without promising algorithmic reach.",
            },
            {
                "id": "google_business_management",
                "title": "Google Business Profile management",
                "description": "Maintain approved listings, publish updates and draft professional review responses; never fabricate reviews.",
            },
        ],
    },
    {
        "id": "growth",
        "title": "Campaigns, partnerships & insights",
        "icon": "chart-no-axes-combined",
        "description": "Test thoughtfully and use reporting to guide the next decision.",
        "services": [
            {
                "id": "paid_social",
                "title": "Paid social advertising",
                "description": "Scope Meta, LinkedIn or other supported campaigns with agreed objectives, budgets and separate media spend.",
            },
            {
                "id": "lead_generation",
                "title": "Lead-generation campaigns",
                "description": "Plan offers, campaign creatives and enquiry journeys; lead volume and quality are not guaranteed.",
            },
            {
                "id": "influencer_collaboration",
                "title": "Influencer & creator collaborations",
                "description": "Research suitable creators, coordinate briefs and disclosure requirements, and quote creator fees separately.",
            },
            {
                "id": "ugc",
                "title": "UGC coordination",
                "description": "Coordinate user-generated content briefs, permissions and deliverables with participating creators.",
            },
            {
                "id": "analytics_reporting",
                "title": "Analytics & performance reporting",
                "description": "Summarize available platform metrics against agreed goals with context rather than unsupported claims.",
            },
            {
                "id": "optimization",
                "title": "Campaign optimization & consultation",
                "description": "Review content and campaign signals, recommend experiments and provide scheduled strategy consultations.",
            },
        ],
    },
]

PROCESS_STEPS: list[EditorialItem] = [
    {
        "id": "discover",
        "title": "Discover & align",
        "description": "Discuss the business, audience, goals, current channels and scope; agree on responsibilities and success measures.",
        "icon": "messages-square",
    },
    {
        "id": "plan",
        "title": "Build the plan",
        "description": "Create content pillars, visual direction and a calendar with clear deliverables and approval checkpoints.",
        "icon": "notebook-pen",
    },
    {
        "id": "create",
        "title": "Create, approve & publish",
        "description": "Develop assets, gather feedback and publish only approved content through authorized channel access.",
        "icon": "send",
    },
    {
        "id": "refine",
        "title": "Measure & refine",
        "description": "Review available metrics, discuss learnings and adjust the next cycle without promising specific outcomes.",
        "icon": "chart-no-axes-combined",
    },
]

PORTFOLIO: list[PortfolioContent] = [
    {
        "id": "cafe_concept",
        "title": "Neighbourhood café — concept direction",
        "industry": "Food & hospitality",
        "platforms": ["instagram", "facebook"],
        "services": ["static_design", "reels_shorts", "content_calendar"],
        "brief": "Illustrative brief: introduce a café menu and its daily rituals.",
        "approach": "Warm typography, ingredient-focused storytelling and a simple weekly content rhythm.",
        "deliverables": [
            "Sample menu carousel",
            "Reel storyboard",
            "Illustrative content calendar",
        ],
        "image_url": "/placeholder.svg",
        "image_alt": "Placeholder for a demo café creative concept; not actual client work.",
        "is_demo": True,
        "demo_label": "Demo concept — not client work",
        "disclaimer": "Fictional concept only. No commissioned client, campaign results or business endorsement is implied.",
    },
    {
        "id": "wellness_concept",
        "title": "Wellness studio — concept direction",
        "industry": "Wellness & fitness",
        "platforms": ["instagram", "pinterest"],
        "services": ["brand_voice", "stories", "static_design"],
        "brief": "Illustrative brief: explain a studio experience with approachable, non-medical content.",
        "approach": "Calm visual templates, helpful introductory content and clear class information.",
        "deliverables": [
            "Sample educational carousel",
            "Story sequence",
            "Pin concepts",
        ],
        "image_url": "/placeholder.svg",
        "image_alt": "Placeholder for a demo wellness creative concept; not actual client work.",
        "is_demo": True,
        "demo_label": "Demo concept — not client work",
        "disclaimer": "Fictional concept only. No commissioned client, campaign results or health outcomes are implied.",
    },
    {
        "id": "b2b_concept",
        "title": "Professional services — concept direction",
        "industry": "Professional services",
        "platforms": ["linkedin", "youtube"],
        "services": ["social_strategy", "copywriting", "youtube_packaging"],
        "brief": "Illustrative brief: make specialist knowledge easier to understand.",
        "approach": "An expertise-led editorial series, readable document posts and explanatory video packaging.",
        "deliverables": [
            "Sample LinkedIn document",
            "Thought-leadership outline",
            "Thumbnail concept",
        ],
        "image_url": "/placeholder.svg",
        "image_alt": "Placeholder for a demo professional-services concept; not actual client work.",
        "is_demo": True,
        "demo_label": "Demo concept — not client work",
        "disclaimer": "Fictional concept only. No commissioned client, campaign results or business endorsement is implied.",
    },
]

INDUSTRIES: list[IndustryContent] = [
    {"id": "food", "label": "Food & hospitality", "icon": "utensils"},
    {"id": "fashion", "label": "Fashion & lifestyle", "icon": "shirt"},
    {"id": "beauty", "label": "Beauty & personal care", "icon": "sparkles"},
    {"id": "wellness", "label": "Wellness & fitness", "icon": "heart"},
    {"id": "retail", "label": "Retail & e-commerce", "icon": "shopping-bag"},
    {"id": "real_estate", "label": "Real estate", "icon": "house"},
    {
        "id": "education",
        "label": "Education & training",
        "icon": "graduation-cap",
    },
    {
        "id": "professional",
        "label": "Professional services",
        "icon": "briefcase-business",
    },
    {"id": "technology", "label": "Technology & startups", "icon": "laptop"},
    {"id": "travel", "label": "Travel & experiences", "icon": "plane"},
    {"id": "local", "label": "Local businesses", "icon": "store"},
    {"id": "personal_brand", "label": "Personal brands", "icon": "user"},
]

BENEFITS: list[EditorialItem] = [
    {
        "id": "clarity",
        "title": "A clearer direction",
        "description": "Connect content decisions to audience needs and agreed business goals.",
        "icon": "compass",
    },
    {
        "id": "consistency",
        "title": "A consistent brand voice",
        "description": "Use shared creative and tone guidelines across selected channels.",
        "icon": "palette",
    },
    {
        "id": "time",
        "title": "More room for your business",
        "description": "Reduce ad hoc content coordination with a planned workflow and clear responsibilities.",
        "icon": "clock",
    },
    {
        "id": "community",
        "title": "Thoughtful audience care",
        "description": "Support relevant conversations through agreed response guidelines and escalation paths.",
        "icon": "messages-square",
    },
    {
        "id": "visibility",
        "title": "Useful performance visibility",
        "description": "Understand available metrics through contextual reporting and practical recommendations.",
        "icon": "chart-no-axes-combined",
    },
    {
        "id": "adaptability",
        "title": "A plan that can evolve",
        "description": "Refine content and scope as priorities change, with changes agreed before delivery.",
        "icon": "sliders-horizontal",
    },
]

BEFORE_AFTER: list[ComparisonContent] = [
    {
        "id": "planning",
        "topic": "Planning",
        "before": "Posting whenever an idea appears",
        "after": "An agreed calendar with content pillars and approval dates",
    },
    {
        "id": "identity",
        "topic": "Brand identity",
        "before": "Disconnected visuals and inconsistent tone",
        "after": "Shared templates and a documented brand voice",
    },
    {
        "id": "channels",
        "topic": "Channel focus",
        "before": "Trying to publish everywhere without priorities",
        "after": "Selected platforms matched to audience and resources",
    },
    {
        "id": "approvals",
        "topic": "Approvals",
        "before": "Last-minute feedback scattered across messages",
        "after": "Defined review checkpoints and revision boundaries",
    },
    {
        "id": "community",
        "topic": "Community care",
        "before": "Unclear ownership of comments and enquiries",
        "after": "Agreed response responsibilities and escalation rules",
    },
    {
        "id": "measurement",
        "topic": "Measurement",
        "before": "Looking at isolated likes without context",
        "after": "Reviewing relevant metrics against agreed goals",
    },
]
BEFORE_AFTER_NOTICE: str = "Illustrative workflow comparison, not measured before-and-after client results."

TESTIMONIALS: list[TestimonialContent] = [
    {
        "id": "demo_planning",
        "quote": "The monthly calendar would help our team see what needs approval before the week begins.",
        "attribution": "Fictional business owner",
        "role": "Illustrative planning feedback",
        "is_demo": True,
        "demo_label": "Demo testimonial — fictional quotation",
        "disclaimer": "Sample copy for layout planning, not a statement from a real customer or evidence of results.",
    },
    {
        "id": "demo_creative",
        "quote": "A shared visual direction would make it easier to keep our social content consistent.",
        "attribution": "Fictional brand manager",
        "role": "Illustrative creative feedback",
        "is_demo": True,
        "demo_label": "Demo testimonial — fictional quotation",
        "disclaimer": "Sample copy for layout planning, not a statement from a real customer or evidence of results.",
    },
    {
        "id": "demo_reporting",
        "quote": "A clear review of what we learned would make our next content discussion more focused.",
        "attribution": "Fictional founder",
        "role": "Illustrative reporting feedback",
        "is_demo": True,
        "demo_label": "Demo testimonial — fictional quotation",
        "disclaimer": "Sample copy for layout planning, not a statement from a real customer or evidence of results.",
    },
]

FAQS: list[FAQContent] = [
    {
        "id": "services",
        "question": "What services can be included?",
        "answer": "The draft offering covers strategy, content production, publishing, community management, campaigns and reporting. Each engagement will have an agreed scope; the service catalogue does not mean every service is included in every plan.",
    },
    {
        "id": "platforms",
        "question": "Which platforms can you support?",
        "answer": "The proposed catalogue covers Instagram, Facebook, LinkedIn, YouTube, X, Pinterest and Google Business Profile. Select channels based on audience, goals, access requirements and the agreed plan.",
    },
    {
        "id": "plan_selection",
        "question": "How do I choose Basic, Standard or Premium?",
        "answer": "Compare the draft platform coverage, content volumes and support listed in each plan. Standard is the highlighted editorial recommendation, not a claimed best seller. Confirm your needs and final scope before purchasing.",
    },
    {
        "id": "durations",
        "question": "How do Monthly, 6 Months and 1 Year prices work?",
        "answer": "Each listed INR amount is the total service fee for the selected duration, not a monthly payment. Monthly covers one month, 6 Months covers six and 1 Year covers twelve. Prices and any savings labels are editable draft values, not a live offer.",
    },
    {
        "id": "custom",
        "question": "Can I request a custom plan?",
        "answer": "The custom-plan enquiry form can specify platforms, content volumes, goals, budget and timeline. A tailored scope and quotation must be agreed before work begins; enquiry submission is not an order.",
    },
    {
        "id": "onboarding",
        "question": "What will you need to get started?",
        "answer": "Typically a business brief, audience information, brand assets, product details and authorized platform access. Do not send account passwords through an enquiry form; use the platform's role-based access tools.",
    },
    {
        "id": "approval",
        "question": "Will I approve content before it is published?",
        "answer": "The proposed workflow includes calendar and creative approval checkpoints. Publication should follow explicit approval; revision limits, approval windows and delays must be recorded in the final scope.",
    },
    {
        "id": "production",
        "question": "Are photography and video shoots included?",
        "answer": "The draft plans use client-supplied assets and footage. On-location shoots, travel, specialist production and licensing are separately scoped and quoted unless expressly included in a written agreement.",
    },
    {
        "id": "ads",
        "question": "Are advertising budgets and creator fees included?",
        "answer": "No. Draft service prices exclude advertising spend, creator or influencer fees, paid tools and third-party licences. Campaign management is included only where expressly agreed, with media budgets approved separately.",
    },
    {
        "id": "results",
        "question": "Can you guarantee followers, leads or sales?",
        "answer": "No. Outcomes depend on the offer, audience, budget, market and platform behaviour. The proposed service focuses on consistent delivery, informed testing and transparent reporting; it does not promise follower counts, viral reach or sales.",
    },
    {
        "id": "reporting",
        "question": "How will performance be reported?",
        "answer": "Draft plans include a monthly review of available platform metrics with context and next steps. Final reporting measures and review cadence will be agreed during onboarding; access limitations may affect which metrics are available.",
    },
    {
        "id": "payment_terms",
        "question": "How will payment, taxes and cancellations be handled?",
        "answer": "Checkout is held while sample pricing and commercial terms await owner approval. Draft Privacy, Terms and Refund / Cancellation pages are now available, but publication is not commercial approval. The owner must verify business details, approve final prices, taxes and terms, and configure Razorpay before payment can be accepted. No cancellation or refund entitlement is promised by this draft copy.",
    },
    {
        "id": "demo_content",
        "question": "Are the portfolio projects and testimonials real?",
        "answer": "No. All current portfolio entries are fictional creative concepts and all testimonials are demo quotations, clearly labelled as such. They do not represent client work, endorsements or measured results. Contact and social details remain non-clickable placeholders pending verification. The contact form can save a general enquiry, but submission does not verify the agency or guarantee a reply.",
    },
]

PRICING: PricingContent = {
    "currency": "INR",
    "price_basis": "Total service fee for the entire selected duration; integer rupees, not monthly instalments.",
    "default_duration_id": "monthly",
    "default_plan_id": "standard",
    "is_draft": True,
    "approved_for_checkout": False,
    "notice": "Illustrative editable pricing and deliverables only; not an approved offer. Verify scope, prices, taxes and legal terms before enabling checkout.",
    "tax_notice": "Applicable taxes and invoicing treatment must be confirmed before publication; no tax rate is assumed here.",
    "exclusions": [
        "Advertising/media spend",
        "Influencer and creator fees",
        "On-location shoots and travel",
        "Paid stock, tools and third-party licences",
        "Services not expressly included in the agreed scope",
    ],
    "custom_plan_title": "A plan shaped around your needs",
    "custom_plan_description": "Share your preferred channels, content requirements, goals, budget and timeline for a separately agreed quotation.",
    "durations": [
        {"id": "monthly", "label": "Monthly", "months": 1},
        {"id": "six_months", "label": "6 Months", "months": 6},
        {"id": "one_year", "label": "1 Year", "months": 12},
    ],
    "plans": [
        {
            "id": "basic",
            "name": "Basic",
            "description": "A focused starting point for a consistent social presence.",
            "highlighted": False,
            "highlight_label": "",
            "features": [
                "Management of 2 agreed platforms",
                "8 static posts or carousels per month",
                "2 short-form video edits per month from supplied footage",
                "8 story frames per month",
                "Monthly content calendar and captions",
                "Profile optimization during onboarding",
                "1 consolidated revision round per content batch",
                "Monthly performance summary",
            ],
            "prices": {
                "monthly": {"total_inr": 9999, "savings_label": ""},
                "six_months": {
                    "total_inr": 51000,
                    "savings_label": "Save ₹8,994 versus six Monthly periods",
                },
                "one_year": {
                    "total_inr": 96000,
                    "savings_label": "Save ₹23,988 versus twelve Monthly periods",
                },
            },
        },
        {
            "id": "standard",
            "name": "Standard",
            "description": "A balanced draft scope for broader storytelling and audience care.",
            "highlighted": True,
            "highlight_label": "MOST POPULAR",
            "features": [
                "Management of 3 agreed platforms",
                "12 static posts or carousels per month",
                "4 short-form video edits per month from supplied footage",
                "12 story frames per month",
                "Monthly strategy-led calendar and captions",
                "Profile optimization during onboarding",
                "Community response support within agreed hours",
                "2 consolidated revision rounds per content batch",
                "Monthly performance report and review call",
            ],
            "prices": {
                "monthly": {"total_inr": 19999, "savings_label": ""},
                "six_months": {
                    "total_inr": 84000,
                    "savings_label": "Save ₹35,994 versus six Monthly periods",
                },
                "one_year": {
                    "total_inr": 156000,
                    "savings_label": "Save ₹83,988 versus twelve Monthly periods",
                },
            },
        },
        {
            "id": "premium",
            "name": "Premium",
            "description": "A more involved draft scope for multi-channel creative coordination.",
            "highlighted": False,
            "highlight_label": "",
            "features": [
                "Management of 4 agreed platforms",
                "16 static posts or carousels per month",
                "8 short-form video edits per month from supplied footage",
                "20 story frames per month",
                "Monthly strategy-led calendar and campaign concepts",
                "Profile optimization during onboarding",
                "Community response support within agreed hours",
                "2 consolidated revision rounds per content batch",
                "Monthly performance report and 2 review calls",
                "Paid campaign planning consultation; execution quoted separately",
            ],
            "prices": {
                "monthly": {"total_inr": 34999, "savings_label": ""},
                "six_months": {
                    "total_inr": 138000,
                    "savings_label": "Save ₹71,994 versus six Monthly periods",
                },
                "one_year": {
                    "total_inr": 252000,
                    "savings_label": "Save ₹167,988 versus twelve Monthly periods",
                },
            },
        },
    ],
}

PLAN_FEATURE_NOTICE: str = "Draft monthly content volumes. Adaptation across selected platforms does not multiply asset counts. Story counts mean individual frames. Community hours, turnaround times and final deliverables require written agreement."
