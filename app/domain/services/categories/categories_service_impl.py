from typing import List
from uuid import UUID

from app.domain.models.category import Category
from app.domain.repositories.categories_repository import CategoriesRepository
from app.domain.services.categories.categories_service import CategoriesService
from app.domain.services.categories.dependencies import CategoriesRepositoryDep
from app.domain.services.categories.exceptions import CategoryAlreadyExists, CategoryDoesNotExist
from app.domain.services.categories.schemas import CreateCategoryDTO


class CategoriesServiceImpl(CategoriesService):
    categories_repository: CategoriesRepository

    def __init__(self, categories_repository: CategoriesRepositoryDep):
        self.categories_repository = categories_repository

    def get_all(self) -> List[Category]:
        categories = self.categories_repository.get_all()
        return categories if categories else []

    def get_by_id(self, id: UUID) -> Category:
        category = self.categories_repository.get_by_id(id)
        if not category:
            raise CategoryDoesNotExist()
        return category

    def create(self, data: CreateCategoryDTO) -> Category:
        current_category = self.categories_repository.get_by_name(data.name)
        if current_category:
            raise CategoryAlreadyExists()
        category = Category(id=None, name=data.name)
        saved_category = self.categories_repository.create(category)
        return saved_category

    def delete(self, id: UUID):
        category = self.categories_repository.get_by_id(id)
        if not category:
            raise CategoryDoesNotExist()
        self.categories_repository.delete(category)
