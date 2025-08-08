from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from app.domain.models.location import BaseLocation


class LocationEntity(SQLModel, BaseLocation, table=True):
    __tablename__ = 'locations'
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    category_id: UUID = Field(foreign_key="categories.id", default=None)
    category: "CategoryEntity" = Relationship(back_populates="locations")
    reviews: list["ReviewEntity"] = Relationship(back_populates="location")
