from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from app.domain.models.category import Category


class CategoryEntity(SQLModel, Category, table=True):
    __tablename__ = 'categories'
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    locations: list["LocationEntity"] = Relationship(back_populates="category")
