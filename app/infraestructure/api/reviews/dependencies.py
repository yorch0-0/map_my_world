from typing import Annotated

from fastapi import Depends

from app.domain.services.reviews.review_service import ReviewsService
from app.domain.services.reviews.reviews_service_impl import ReviewsServiceImpl

ReviewsServiceDep = Annotated[ReviewsService, Depends(ReviewsServiceImpl)]
