from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.domain.models.location import Location
from app.domain.services.locations.schemas import CreateLocationDTO


class LocationsService(ABC):
    @abstractmethod
    def get_all(self) -> List[Location]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Location:
        pass

    @abstractmethod
    def create(self, data: CreateLocationDTO) -> Location:
        pass

    @abstractmethod
    def delete(self, id: UUID):
        pass

    @abstractmethod
    def get_recommendations(self) -> List[Location]:
        pass