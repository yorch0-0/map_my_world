from typing import Annotated

from fastapi.params import Depends

from app.domain.services.locations.locations_service import LocationsService
from app.domain.services.locations.locations_service_impl import LocationsServiceImpl

LocationsServiceDep = Annotated[LocationsService, Depends(LocationsServiceImpl)]
