from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.domain.models.location import Location
from app.domain.repositories.base_repository import BaseRepository


class LocationsRepository(BaseRepository[Location, UUID], ABC):
    @abstractmethod
    def get_recommended_locations(self) -> List[Location]:
        pass
