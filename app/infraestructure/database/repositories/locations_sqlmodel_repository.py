from datetime import datetime, timedelta

from sqlmodel import select, func, or_

from app.domain.models.location import Location
from app.domain.repositories.locations_repository import LocationsRepository
from app.infraestructure.database.entities import LocationEntity, ReviewEntity
from app.infraestructure.database.repositories.base_sqlmodel_repository import BaseSqlModelRepository


class LocationsSqlModelRepository(LocationsRepository, BaseSqlModelRepository):
    def get_all(self):
        return self.db_session.exec(select(LocationEntity)).all()

    def get_by_id(self, item_id):
        db_item = self.db_session.exec(select(LocationEntity).where(LocationEntity.id == item_id)).first()
        if not db_item:
            return None
        return LocationEntity(**db_item.__dict__)

    def create(self, item):
        location = LocationEntity(**item.__dict__)
        self.db_session.add(location)
        self.db_session.commit()
        self.db_session.refresh(location)
        return Location(**location.__dict__)

    def update(self, item):
        pass

    def delete(self, item):
        location = LocationEntity(**item.__dict__)
        location = self.db_session.merge(location)
        self.db_session.delete(location)
        self.db_session.commit()

    def get_recommended_locations(self):
        latest_review_subquery = select(ReviewEntity.location_id,
                                        func.max(ReviewEntity.created_at).label("latest_review_date")).group_by(
            ReviewEntity.location_id).subquery()
        thirty_days_ago = datetime.now() - timedelta(days=30)
        statement = select(LocationEntity).join(latest_review_subquery,
                                                LocationEntity.id == latest_review_subquery.c.location_id,
                                                isouter=True, full=True).order_by(
            latest_review_subquery.c.latest_review_date.asc().nulls_first()).where(
            or_(latest_review_subquery.c.latest_review_date > thirty_days_ago,
                latest_review_subquery.c.latest_review_date.is_(None))
            ).limit(10)
        return self.db_session.exec(statement).all()
