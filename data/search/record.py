
from collections import namedtuple

Record = namedtuple("Record", ['id', 'short_text', 'large_text', 'number'])


class RecordPlaceholder:

    def __init__(self, short_text, large_text, number):
        self.short_text = short_text
        self.large_text = large_text
        self.number = number
