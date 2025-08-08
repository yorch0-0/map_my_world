from typing import Annotated

from fastapi.params import Depends

from app.domain.repositories.locations_repository import LocationsRepository
from app.domain.services.categories.categories_service import CategoriesService
from app.domain.services.categories.categories_service_impl import CategoriesServiceImpl
from app.infraestructure.database.repositories.locations_sqlmodel_repository import LocationsSqlModelRepository

LocationsRepositoryDep = Annotated[LocationsRepository, Depends(LocationsSqlModelRepository)]
CategoriesServiceDep = Annotated[CategoriesService, Depends(CategoriesServiceImpl)]
