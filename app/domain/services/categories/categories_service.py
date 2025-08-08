from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.domain.models.category import Category
from app.domain.services.categories.schemas import CreateCategoryDTO


class CategoriesService(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Category:
        pass

    @abstractmethod
    def create(self, data: CreateCategoryDTO) -> Category:
        pass

    @abstractmethod
    def delete(self, id: UUID):
        pass