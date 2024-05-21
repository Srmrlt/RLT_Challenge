import logging

from app.database import Mongo

from .data_handler import DataHandler
from .input_handler import InputHandler
from .output_handler import OutputProcessor
from .search_handler import SearchHandler

logger = logging.getLogger(__name__)


class DataPipeline:
    def __init__(self, input_str: str):
        self.input_str = input_str

    async def execute(self):
        input_data = InputHandler(self.input_str).extract_data()
        intervals = SearchHandler(input_data).generate_intervals()
        mongo_instance = Mongo()

        await mongo_instance.connect_db_collection()
        if await mongo_instance.check_connection():
            output_processor = OutputProcessor()
            for interval in intervals:
                total = DataHandler()
                async for el in mongo_instance.find_by_datetime_range(**interval):
                    total.accumulate_value(el)
                output_processor.store_output(interval, total.total)
            await mongo_instance.close_db()
            return output_processor.get_output()
        logger.error("Failed to connect to MongoDB")
        raise ConnectionError("Failed to connect to MongoDB")
