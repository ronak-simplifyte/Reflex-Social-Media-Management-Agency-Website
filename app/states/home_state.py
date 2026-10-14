import reflex as rx

from app.content import (
    PORTFOLIO,
    SERVICE_CATEGORIES,
    PortfolioContent,
    ServiceContent,
)


class HomeState(rx.State):
    theme: str = rx.LocalStorage("light", name="atelier-theme")
    service_tab: str = "Content"
    portfolio_filter: str = "All"

    @rx.event
    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"

    @rx.event
    def select_service(self, tab: str):
        if tab in ("Content", "Management", "Strategy", "Growth", "Creative"):
            self.service_tab = tab

    @rx.event
    def select_portfolio(self, category: str):
        if category in (
            "All",
            "Instagram",
            "Reels",
            "Branding",
            "LinkedIn",
            "Facebook",
            "YouTube",
        ):
            self.portfolio_filter = category

    @rx.var
    def active_services(self) -> list[ServiceContent]:
        category_id = {
            "Content": "creative",
            "Creative": "creative",
            "Management": "management",
            "Strategy": "strategy",
            "Growth": "growth",
        }[self.service_tab]
        services = next(
            category["services"]
            for category in SERVICE_CATEGORIES
            if category["id"] == category_id
        )
        if self.service_tab == "Content":
            return services[:4]
        if self.service_tab == "Creative":
            return services[4:]
        return services

    @rx.var
    def service_description(self) -> str:
        category_id = {
            "Content": "creative",
            "Creative": "creative",
            "Management": "management",
            "Strategy": "strategy",
            "Growth": "growth",
        }[self.service_tab]
        return next(
            category["description"]
            for category in SERVICE_CATEGORIES
            if category["id"] == category_id
        )

    @rx.var
    def visible_portfolio(self) -> list[PortfolioContent]:
        if self.portfolio_filter == "All":
            return PORTFOLIO
        if self.portfolio_filter == "Reels":
            return [
                project
                for project in PORTFOLIO
                if "reels_shorts" in project["services"]
            ]
        if self.portfolio_filter == "Branding":
            return [
                project
                for project in PORTFOLIO
                if "brand_voice" in project["services"]
            ]
        return [
            project
            for project in PORTFOLIO
            if self.portfolio_filter.lower() in project["platforms"]
        ]
