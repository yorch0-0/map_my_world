import json

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from app.domain.services.locations.exceptions import LocationDoesNotExist
from app.domain.services.reviews.schemas import CreateReviewDTO
from app.infraestructure.api.reviews.dependencies import ReviewsServiceDep

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/")
def create_review(review: CreateReviewDTO, reviews_service: ReviewsServiceDep):
    try:
        return reviews_service.create(review)
    except LocationDoesNotExist:
        return Response(json.dumps({"message": "Location not found"}), status.HTTP_400_BAD_REQUEST,
                        media_type="application/json")
