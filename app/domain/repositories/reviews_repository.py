from abc import ABC
from uuid import UUID

from app.domain.models.review import Review
from app.domain.repositories.base_repository import BaseRepository


class ReviewsRepository(BaseRepository[Review, UUID], ABC):
    pass
