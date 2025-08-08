from typing import Annotated

from fastapi.params import Depends

from app.domain.services.categories.categories_service import CategoriesService
from app.domain.services.categories.categories_service_impl import CategoriesServiceImpl

CategoriesServiceDep = Annotated[CategoriesService, Depends(CategoriesServiceImpl)]
