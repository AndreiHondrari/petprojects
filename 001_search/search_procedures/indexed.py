
import time

from typing import List, Dict

from record import Record
from search_tools.indexed import index_code


def search_short_text(
    target_record: Record,
    collection: Dict[int, Record],
    short_text_index: Dict[int, List[int]]
) -> None:
    print("#################################################################")
    print(
        "Index search for short text "
        "(for indexed collection): {}\n".format(target_record.short_text)
    )

    start = time.time()

    count = 0
    search_code: int = index_code(target_record.short_text)
    if search_code in short_text_index:
        for record_id in short_text_index[search_code]:
            print("Found record: {}\n".format(collection[record_id]))
            count += 1

    print("Search time: {:.6f}s".format(time.time() - start))
    print("Counted: {}\n".format(count))


def search_long_text(
    target_record: Record,
    collection: Dict[int, Record],
    large_text_index: Dict[int, List[int]]
) -> None:
    print("#################################################################")
    print(
        "Index search for large text "
        "(for indexed collection): {}\n".format(target_record.large_text)
    )

    start = time.time()

    search_code = index_code(target_record.large_text)
    count = 0
    if search_code in large_text_index:
        for record_id in large_text_index[search_code]:
            print("Found record: {}\n".format(collection[record_id]))
            count += 1

    print("Search time: {:.6f}s".format(time.time() - start))
    print("Counted: {}\n".format(count))
