from abc import ABC, abstractmethod

from app.domain.services.reviews.schemas import CreateReviewDTO


class ReviewsService(ABC):
    @abstractmethod
    def create(self, review: CreateReviewDTO):
        pass
