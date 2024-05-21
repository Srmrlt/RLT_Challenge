class DataHandler:
    def __init__(self):
        self.total: int = 0

    @staticmethod
    def extract_value(doc: dict) -> int | None:
        return doc.get("value", None)

    def accumulate_value(self, doc: dict):
        value = self.extract_value(doc)
        if value is not None:
            self.total += value
