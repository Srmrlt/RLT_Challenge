import logging
from datetime import datetime as dt
from datetime import timedelta

from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


class SearchHandler:
    def __init__(self, input_data: dict[str, dt | str]):
        self.dt_from = input_data["dt_from"]
        self.dt_upto = input_data["dt_upto"]
        self.group_type = input_data["group_type"]

    def generate_intervals(self) -> list[dict[str, dt]]:
        intervals = []
        current = self.dt_from
        add_delta = {
            "hour": timedelta(hours=1),
            "day": timedelta(days=1),
            "month": relativedelta(months=1),
            "year": relativedelta(years=1),
        }.get(self.group_type)

        if add_delta is None:
            raise ValueError("Unsupported group_type. Use 'hour', 'day', 'month', or 'year'.")

        while current <= self.dt_upto:
            next_interval = current + add_delta - timedelta(seconds=1)
            intervals.append({"dt_from": current, "dt_upto": min(next_interval, self.dt_upto)})
            current = next_interval + timedelta(seconds=1)

        return intervals
