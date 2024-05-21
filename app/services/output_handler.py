import logging
from datetime import datetime as dt

logger = logging.getLogger(__name__)


class OutputProcessor:
    def __init__(self):
        self.output = {"dataset": [], "labels": []}

    def store_output(self, interval: dict[str, dt], data: int):
        dt_from = dt.isoformat(interval["dt_from"])
        self.output["dataset"].append(data)
        self.output["labels"].append(dt_from)

    def get_output(self):
        return self.output
