"""Persistent enquiry and checkout schemas; no database I/O or schema creation."""

import reflex as rx

from datetime import datetime, timezone

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    DateTime,
    ForeignKey,
    JSON,
    String,
    Text,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Lead(Base):
    __tablename__ = "lead"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(200), default="", server_default=""
    )
    business_name: Mapped[str] = mapped_column(
        String(250), default="", server_default=""
    )
    email: Mapped[str] = mapped_column(
        String(320), default="", server_default="", index=True
    )
    phone: Mapped[str] = mapped_column(
        String(32), default="", server_default=""
    )
    whatsapp: Mapped[str] = mapped_column(
        String(32), default="", server_default=""
    )
    preferred_contact_method: Mapped[str] = mapped_column(
        String(32), default="email", server_default="email"
    )
    subject: Mapped[str] = mapped_column(
        String(250), default="", server_default=""
    )
    message: Mapped[str] = mapped_column(Text, default="", server_default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=func.now(),
    )


class CustomPlanEnquiry(Base):
    __tablename__ = "custom_plan_enquiry"
    __table_args__ = (
        CheckConstraint(
            "budget_min_paise >= 0", name="ck_custom_enquiry_budget_min"
        ),
        CheckConstraint(
            "budget_max_paise >= budget_min_paise",
            name="ck_custom_enquiry_budget_range",
        ),
        CheckConstraint(
            "duration_months >= 1", name="ck_custom_enquiry_duration"
        ),
        CheckConstraint(
            "posts_per_month >= 0 AND reels_per_month >= 0 AND stories_per_month >= 0",
            name="ck_custom_enquiry_content_counts",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(200), default="", server_default=""
    )
    business_name: Mapped[str] = mapped_column(
        String(250), default="", server_default=""
    )
    email: Mapped[str] = mapped_column(
        String(320), default="", server_default="", index=True
    )
    phone: Mapped[str] = mapped_column(
        String(32), default="", server_default=""
    )
    whatsapp: Mapped[str] = mapped_column(
        String(32), default="", server_default=""
    )
    preferred_contact_method: Mapped[str] = mapped_column(
        String(32), default="email", server_default="email"
    )
    website_url: Mapped[str] = mapped_column(
        String(2048), default="", server_default=""
    )
    industry: Mapped[str] = mapped_column(
        String(200), default="", server_default=""
    )
    platforms: Mapped[list[str]] = mapped_column(JSON, default=list)
    services: Mapped[list[str]] = mapped_column(JSON, default=list)
    social_profile_urls: Mapped[list[str]] = mapped_column(JSON, default=list)
    goals: Mapped[str] = mapped_column(Text, default="", server_default="")
    target_audience: Mapped[str] = mapped_column(
        Text, default="", server_default=""
    )
    requirements: Mapped[str] = mapped_column(
        Text, default="", server_default=""
    )
    posts_per_month: Mapped[int] = mapped_column(default=0, server_default="0")
    reels_per_month: Mapped[int] = mapped_column(default=0, server_default="0")
    stories_per_month: Mapped[int] = mapped_column(
        default=0, server_default="0"
    )
    budget_min_paise: Mapped[int] = mapped_column(
        BigInteger, default=0, server_default="0"
    )
    budget_max_paise: Mapped[int] = mapped_column(
        BigInteger, default=0, server_default="0"
    )
    duration_months: Mapped[int] = mapped_column(default=1, server_default="1")
    preferred_start_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
    timeline: Mapped[str] = mapped_column(
        String(250), default="", server_default=""
    )
    message: Mapped[str] = mapped_column(Text, default="", server_default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=func.now(),
    )


class Order(Base):
    __tablename__ = "order"
    __table_args__ = (
        CheckConstraint("amount_paise >= 0", name="ck_order_amount"),
        CheckConstraint("duration_months >= 1", name="ck_order_duration"),
        CheckConstraint("currency = 'INR'", name="ck_order_currency"),
        CheckConstraint(
            "status IN ('pending', 'paid', 'failed', 'cancelled')",
            name="ck_order_status",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(
        String(200), default="", server_default=""
    )
    business_name: Mapped[str] = mapped_column(
        String(250), default="", server_default=""
    )
    phone: Mapped[str] = mapped_column(
        String(32), default="", server_default=""
    )
    whatsapp: Mapped[str] = mapped_column(
        String(32), default="", server_default=""
    )
    email: Mapped[str] = mapped_column(
        String(320), default="", server_default="", index=True
    )
    plan_id: Mapped[str] = mapped_column(
        String(100), default="", server_default=""
    )
    plan_name: Mapped[str] = mapped_column(
        String(200), default="", server_default=""
    )
    duration_months: Mapped[int] = mapped_column(default=1, server_default="1")
    amount_paise: Mapped[int] = mapped_column(
        BigInteger, default=0, server_default="0"
    )
    currency: Mapped[str] = mapped_column(
        String(3), default="INR", server_default="INR"
    )
    status: Mapped[str] = mapped_column(
        String(16), default="pending", server_default="pending", index=True
    )
    provider: Mapped[str] = mapped_column(
        String(32), default="razorpay", server_default="razorpay"
    )
    provider_order_id: Mapped[str | None] = mapped_column(
        String(200), default=None, nullable=True, unique=True
    )
    provider_payment_id: Mapped[str | None] = mapped_column(
        String(200), default=None, nullable=True, unique=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=func.now(),
    )
    paid_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
    failed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
    cancelled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )


class PaymentAttempt(Base):
    __tablename__ = "payment_attempt"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'paid', 'failed', 'cancelled')",
            name="ck_payment_attempt_status",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int | None] = mapped_column(
        ForeignKey("order.id", ondelete="RESTRICT"),
        default=None,
        nullable=True,
        index=True,
        comment="Local order association; nullable for migration-safe historical records.",
    )
    provider: Mapped[str] = mapped_column(
        String(32), default="razorpay", server_default="razorpay"
    )
    provider_order_id: Mapped[str | None] = mapped_column(
        String(200), default=None, nullable=True, index=True
    )
    provider_payment_id: Mapped[str | None] = mapped_column(
        String(200), default=None, nullable=True, unique=True
    )
    status: Mapped[str] = mapped_column(
        String(16), default="pending", server_default="pending", index=True
    )
    error_code: Mapped[str] = mapped_column(
        String(100), default="", server_default=""
    )
    error_reason: Mapped[str] = mapped_column(
        String(200), default="", server_default=""
    )
    error_source: Mapped[str] = mapped_column(
        String(100), default="", server_default=""
    )
    error_step: Mapped[str] = mapped_column(
        String(100), default="", server_default=""
    )
    error_description: Mapped[str] = mapped_column(
        String(500),
        default="",
        server_default="",
        comment="Sanitized summary only: no raw payloads, credentials, signatures, card details or customer PII.",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=func.now(),
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
