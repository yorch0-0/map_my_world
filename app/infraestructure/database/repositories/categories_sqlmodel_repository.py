from sqlmodel import select

from app.domain.models.category import Category
from app.domain.repositories.categories_repository import CategoriesRepository
from app.infraestructure.database.entities import CategoryEntity
from app.infraestructure.database.repositories.base_sqlmodel_repository import BaseSqlModelRepository


class CategoriesSqlModelRepository(CategoriesRepository, BaseSqlModelRepository):
    def get_all(self):
        return self.db_session.exec(select(CategoryEntity)).all()

    def get_by_id(self, item_id):
        db_item = self.db_session.exec(select(CategoryEntity).where(CategoryEntity.id == item_id)).first()
        if not db_item: return None
        return Category(**db_item.__dict__)

    def create(self, item):
        category = CategoryEntity(**item.__dict__)
        self.db_session.add(category)
        self.db_session.commit()
        self.db_session.refresh(category)
        return Category(**category.__dict__)

    def update(self, item):
        pass

    def delete(self, item):
        category = CategoryEntity(**item.__dict__)
        category = self.db_session.merge(category)
        self.db_session.delete(category)
        self.db_session.commit()

    def get_by_name(self, name):
        db_item = self.db_session.exec(select(CategoryEntity).where(CategoryEntity.name == name)).first()
        return db_item
