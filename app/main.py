import uvicorn
from fastapi import FastAPI

from app.infraestructure.api.categories.router import router as categories_router
from app.infraestructure.api.locations.router import router as locations_router
from app.infraestructure.api.reviews.router import router as reviews_router
from app.infraestructure.database.config import init_db

app = FastAPI(title="Map my world")

app.include_router(categories_router)
app.include_router(locations_router)
app.include_router(reviews_router)


@app.on_event("startup")
def startup():
    init_db()


@app.get('/', tags=['HealthCheck'])
def health_check():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
