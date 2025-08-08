from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.category import Category
from app.domain.repositories.base_repository import BaseRepository


class CategoriesRepository(BaseRepository[Category, UUID], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Category:
        pass
