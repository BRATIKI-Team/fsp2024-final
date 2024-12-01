from typing import List, Type, TypeVar, Optional, Generic
from pydantic import BaseModel

from app.data.repositories.base_repository import BaseRepository

T = TypeVar("T", bound=BaseModel)

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def create(self, item: T) -> str:
        """Create a new item using the repository's insert method."""
        return await self.repository.insert(item)

    async def delete(self, item_id: str) -> bool:
        """Delete an item by its ID."""
        return await self.repository.delete(item_id)

    async def update(self, item_id: str, item: T) -> bool:
        """Update an existing item by its ID."""
        return await self.repository.update(item_id, item)

    async def get(self, item_id: str) -> Optional[T]:
        """Get an item by its ID."""
        return await self.repository.get(item_id)

    async def get_all(self) -> List[T]:
        """All items in collection"""
        return await self.repository.get_all()

    async def filter(self, filters: dict) -> List[T]:
        """Filter items based on the given filters."""
        return await self.repository.filter(filters)
