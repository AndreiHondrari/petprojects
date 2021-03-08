
from collections import namedtuple

Record = namedtuple("Record", ['id', 'short_text', 'large_text', 'number'])


class RecordPlaceholder:

    def __init__(
        self,
        short_text: str,
        large_text: str,
        number: int
    ) -> None:
        self.short_text = short_text
        self.large_text = large_text
        self.number = number
