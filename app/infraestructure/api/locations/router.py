import json
from typing import List
from uuid import UUID

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from app.domain.models.location import Location
from app.domain.services.categories.exceptions import CategoryDoesNotExist
from app.domain.services.locations.exceptions import LocationDoesNotExist
from app.domain.services.locations.schemas import CreateLocationDTO
from app.infraestructure.api.locations.dependencies import LocationsServiceDep

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("/", response_model=List[Location])
def get_all(locations_service: LocationsServiceDep):
    return locations_service.get_all()


@router.post("/", response_model=Location)
def create(locations_service: LocationsServiceDep, location: CreateLocationDTO):
    try:
        location = locations_service.create(location)
        return location
    except CategoryDoesNotExist:
        return Response(json.dumps({"message": f'The category with id {id} does not exist'}),
                        status_code=status.HTTP_400_BAD_REQUEST, media_type="application/json")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: UUID, locations_service: LocationsServiceDep):
    try:
        locations_service.delete(id)
    except LocationDoesNotExist:
        return Response(json.dumps({"message": f'The location with id {id} does not exist'}),
                        status_code=status.HTTP_400_BAD_REQUEST, media_type="application/json")


@router.get("/recommended", response_model=List[Location])
def get_recommended_locations(locations_service: LocationsServiceDep):
    return locations_service.get_recommendations()
