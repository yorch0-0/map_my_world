from typing import Annotated

from fastapi import Depends

from app.domain.repositories.reviews_repository import ReviewsRepository
from app.domain.services.locations.locations_service import LocationsService
from app.domain.services.locations.locations_service_impl import LocationsServiceImpl
from app.infraestructure.database.repositories.reviews_sqlmodel_repository import ReviewsSqlModelRepository

ReviewsRepositoryDep = Annotated[ReviewsRepository, Depends(ReviewsSqlModelRepository)]
LocationsServiceDep = Annotated[LocationsService, Depends(LocationsServiceImpl)]
