from typing import List
from uuid import UUID

from app.domain.models.location import Location, BaseLocation
from app.domain.repositories.locations_repository import LocationsRepository
from app.domain.services.categories.categories_service import CategoriesService
from app.domain.services.locations.dependencies import LocationsRepositoryDep, CategoriesServiceDep
from app.domain.services.locations.exceptions import LocationDoesNotExist
from app.domain.services.locations.locations_service import LocationsService
from app.domain.services.locations.schemas import CreateLocationDTO


class LocationsServiceImpl(LocationsService):
    locations_repository: LocationsRepository
    categories_service: CategoriesService

    def __init__(self, locations_repository: LocationsRepositoryDep, categories_service: CategoriesServiceDep):
        self.locations_repository = locations_repository
        self.categories_service = categories_service

    def get_all(self) -> List[Location]:
        locations = self.locations_repository.get_all()
        return locations if locations else []

    def get_by_id(self, id: UUID) -> Location:
        location = self.locations_repository.get_by_id(id)
        if not location:
            raise LocationDoesNotExist
        return location

    def create(self, data: CreateLocationDTO) -> Location:
        self.categories_service.get_by_id(data.category_id)
        location = BaseLocation(id=None, **data.__dict__)
        return self.locations_repository.create(location)

    def delete(self, id: UUID):
        location = self.locations_repository.get_by_id(id)
        if not location:
            raise LocationDoesNotExist()
        self.locations_repository.delete(location)

    def get_recommendations(self) -> List[Location]:
        locations = self.locations_repository.get_recommended_locations()
        return locations if locations else []
