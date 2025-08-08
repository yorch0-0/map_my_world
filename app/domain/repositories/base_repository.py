from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')
K = TypeVar('K')


class BaseRepository(ABC, Generic[T, K]):
    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, item_id: K) -> T | None:
        pass

    @abstractmethod
    def create(self, item: T) -> T:
        pass

    @abstractmethod
    def update(self, item: T) -> T:
        pass

    @abstractmethod
    def delete(self, item: T) -> None:
        pass