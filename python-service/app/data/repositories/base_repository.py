from fastapi.routing import serialize_response
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from typing import List, Dict, Optional, Type, TypeVar, Any, Annotated
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)  # TypeVar for generic models

class BaseRepository:
    def __init__(
            self,
            db: AsyncIOMotorDatabase,
            collection_name: str,
            model_cls: Type[T]):
        self.collection = db[collection_name]
        self.model_cls = model_cls

    async def insert(self, item: T) -> str:
        """Insert a new document into the collection."""
        result = await self.collection.insert_one(item.model_dump(exclude_unset=True))
        return str(result.inserted_id)

    async def delete(self, item_id: str) -> bool:
        """Delete a document by ID."""
        result = await self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count > 0  # Return True if the item was deleted

    async def update(self, item_id: str, item: T) -> bool:
        """Update an existing document by ID."""
        result = await self.collection.update_one(
            {"_id": item_id},
            {"$set": item.model_dump(by_alias=True)}
        )
        return result.modified_count > 0  # Return True if the document was updated

    async def get(self, item_id: str) -> Optional[T]:
        """Get a document by ID."""
        document = await self.collection.find_one({"_id": ObjectId(item_id)})
        if document:
            return self._document_to_model(dict(document))
        return document

    async def get_all(self) -> List[T]:
        documents = await self.collection.find().to_list(None)
        return [self._document_to_model(doc) for doc in documents]

    async def filter(self, filters: Dict[str, Any]) -> List[T]:
        """Filter documents based on given filters."""
        documents = await self.collection.find(filters).to_list()
        return [self._document_to_model(doc) for doc in documents]

    def _document_to_model(self, document: Dict):
        """Convert MongoDB document to Pydantic model."""
        document["id"] = str(document["_id"])
        del document["_id"]
        return self.serialize(document)

    def serialize(self, document: Dict) -> T:
        raise "Method has to be implemented in child repository"