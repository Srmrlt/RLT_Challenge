import json
import logging
from datetime import datetime as dt

logger = logging.getLogger(__name__)


class InputHandler:
    def __init__(self, input_str: str):
        self.input_str: str = input_str
        self.data: dict | None = None

    def extract_data(self) -> dict[str, dt | str]:
        self.parse_json()
        self.validate_input()
        self.convert_dates()
        self.validate_group_type()
        return self.data

    def parse_json(self):
        try:
            self.data = json.loads(self.input_str)
        except json.JSONDecodeError as e:
            logger.error(f"The string you entered is not a valid JSON string: {e}")
            raise ValueError(f"The string you entered is not a valid JSON string: {e}")

    def validate_input(self):
        required_keys = ["dt_from", "dt_upto", "group_type"]
        for key in required_keys:
            if key not in self.data:
                logger.error(f"Missing a required field: {key}")
                raise ValueError(f"Missing a required field: {key}")

    def convert_dates(self):
        try:
            self.data["dt_from"] = dt.fromisoformat(self.data["dt_from"])
            self.data["dt_upto"] = dt.fromisoformat(self.data["dt_upto"])
            if self.data["dt_from"] > self.data["dt_upto"]:
                logger.error("dt_from must be older than dt_upto")
                raise ValueError("dt_from must be greater than dt_upto")
        except ValueError:
            logger.error("Incorrect date format. ISO date format expected")
            raise

    def validate_group_type(self):
        valid_group_types = ["day", "week", "month", "year"]
        if self.data["group_type"] not in valid_group_types:
            logger.error("Invalid group_type value. Expected values: 'day', 'week', 'month', 'year'")
            raise ValueError("Invalid group_type value. Expected values: 'day', 'week', 'month', 'year'")
