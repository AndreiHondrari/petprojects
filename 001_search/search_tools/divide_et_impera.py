
from record import Record

from typing import List


def find_records(
    collection: List[Record],
    attribute: str,
    value: str,
    inner: bool = False
) -> List[Record]:

    if len(collection) == 0:
        return []

    records = []

    middle = len(collection) // 2

    first_half = collection[0:middle]
    middle_element = collection[middle]
    second_half = collection[middle + 1:]
    middle_value = getattr(middle_element, attribute)

    if middle_value == value:
        records.append(middle_element)
        records.extend(find_records(first_half, attribute, value, True))
        records.extend(find_records(second_half, attribute, value, True))

    else:
        if middle_value > value:
            records.extend(find_records(first_half, attribute, value, True))
        elif middle_value < value:
            records.extend(find_records(second_half, attribute, value, True))

    return records
