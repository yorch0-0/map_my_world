from app.domain.models.review import BaseReview
from app.domain.repositories.reviews_repository import ReviewsRepository
from app.infraestructure.database.entities import ReviewEntity
from app.infraestructure.database.repositories.base_sqlmodel_repository import BaseSqlModelRepository


class ReviewsSqlModelRepository(ReviewsRepository, BaseSqlModelRepository):
    def get_all(self):
        pass

    def get_by_id(self, item_id):
        pass

    def create(self, item):
        review = ReviewEntity(**item.__dict__)
        self.db_session.add(review)
        self.db_session.commit()
        self.db_session.refresh(review)
        return BaseReview(**review.__dict__)

    def update(self, item):
        pass

    def delete(self, item):
        pass
