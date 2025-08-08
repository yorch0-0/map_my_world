from typing import Annotated

from fastapi.params import Depends

from app.domain.repositories.categories_repository import CategoriesRepository
from app.infraestructure.database.repositories.categories_sqlmodel_repository import CategoriesSqlModelRepository

CategoriesRepositoryDep = Annotated[CategoriesRepository, Depends(CategoriesSqlModelRepository)]
