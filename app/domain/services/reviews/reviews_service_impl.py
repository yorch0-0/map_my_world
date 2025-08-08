from datetime import datetime

from app.domain.models.review import Review, BaseReview
from app.domain.repositories.reviews_repository import ReviewsRepository
from app.domain.services.locations.locations_service import LocationsService
from app.domain.services.reviews.dependencies import ReviewsRepositoryDep, LocationsServiceDep
from app.domain.services.reviews.review_service import ReviewsService
from app.domain.services.reviews.schemas import CreateReviewDTO


class ReviewsServiceImpl(ReviewsService):
    reviews_repository: ReviewsRepository
    locations_service: LocationsService

    def __init__(self, reviews_repository: ReviewsRepositoryDep, locations_service: LocationsServiceDep):
        self.reviews_repository = reviews_repository
        self.locations_service = locations_service

    def create(self, data: CreateReviewDTO):
        self.locations_service.get_by_id(data.location_id)
        review = BaseReview(id=None, **data.__dict__, created_at=datetime.now())
        return self.reviews_repository.create(review)
