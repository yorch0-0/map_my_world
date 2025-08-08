from typing import List
from uuid import UUID

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from app.domain.models.category import Category
from app.domain.services.categories.exceptions import CategoryAlreadyExists, CategoryDoesNotExist
from app.domain.services.categories.schemas import CreateCategoryDTO
from app.infraestructure.api.categories.dependencies import CategoriesServiceDep

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=List[Category])
def get_all(categories_service: CategoriesServiceDep):
    return categories_service.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Category)
def create(categories_service: CategoriesServiceDep, data: CreateCategoryDTO):
    try:
        category = categories_service.create(data)
        return category
    except CategoryAlreadyExists:
        return Response(status_code=status.HTTP_409_CONFLICT)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: UUID, categories_service: CategoriesServiceDep):
    try:
        categories_service.delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except CategoryDoesNotExist:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
