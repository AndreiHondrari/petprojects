
from record import Record

from typing import Any, List


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


def sort_and_find_records(
    collection: List[Record],
    attribute: str,
    value: Any
) -> List[Record]:
    collection = sorted(
        collection,
        key=lambda x: getattr(x, attribute)  # type: ignore[no-any-return]
    )
    return find_records(collection, attribute, value)
