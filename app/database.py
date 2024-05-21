import logging
from datetime import datetime as dt
from typing import AsyncGenerator

import motor.motor_asyncio
from settings import COLLECTION, DATABASE, DB_HOST, DB_PASS, DB_PORT, DB_USER

logger = logging.getLogger(__name__)


class Mongo:
    def __init__(self):
        self.client = None
        self.collection = None

    async def connect_db_collection(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}"
        )
        db = self.client[DATABASE]
        self.collection = db[COLLECTION]

    async def close_db(self):
        if self.client:
            self.client.close()
            logger.info("Database connection closed.")

    async def check_connection(self):
        try:
            count = await self.collection.estimated_document_count()
            logger.info(f"Connection successful! Collection contains {count} documents.")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to the database: {e}")
            return False

    async def find_by_datetime_range(self, dt_from: dt, dt_upto: dt) -> AsyncGenerator[dict, None]:
        try:
            async for obj in self.collection.find(
                    {"dt": {"$gte": dt_from, "$lte": dt_upto}},
                    {"value": 1, "_id": 0},
            ):
                yield obj
        except Exception as e:
            logger.error(f"Error while querying the database: {e}")
            yield dict()
