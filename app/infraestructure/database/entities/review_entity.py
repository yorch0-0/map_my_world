from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from app.domain.models.review import BaseReview


class ReviewEntity(SQLModel, BaseReview, table=True):
    __tablename__ = 'location_category_reviewed'
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    location_id: UUID = Field(foreign_key="locations.id")
    location: "LocationEntity" = Relationship(back_populates="reviews")