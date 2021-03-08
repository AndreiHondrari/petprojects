
import time

from typing import List

from record import Record
from search_tools.divide_et_impera import find_records


def search_short_text_in_sorted_collection(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Divide et impera search for short text "
        "(for sorted collection): {}\n".format(target_record.short_text)
    )
    before_sort_start = time.time()
    sorted_collection = sorted(
        collection,
        key=lambda x: getattr(x, "short_text")  # type: ignore[no-any-return]
    )
    after_sort_start = time.time()

    found_records = find_records(
        sorted_collection,
        "short_text",
        target_record.short_text
    )

    for r in found_records:
        print("Found record: {}".format(r.id))

    stop = time.time()
    print("\nTotal time: {:.2f}s".format(stop - before_sort_start))
    print("Search time: {:.2f}s".format(stop - after_sort_start))
    print("Counted: {}\n".format(len(found_records)))


def search_long_text_in_sorted_collection(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Divide et impera search for large text "
        "(for post-sorted collection): {}\n".format(target_record.large_text)
    )
    before_sort_start = time.time()
    sorted_collection = sorted(
        collection,
        key=lambda x: getattr(x, "large_text")  # type: ignore[no-any-return]
    )
    after_sort_start = time.time()

    found_records = find_records(
        sorted_collection,
        "large_text",
        target_record.large_text
    )

    for r in found_records:
        print("Found record: {}".format(r.id))

    stop = time.time()
    print("\nTotal time: {:.2f}s".format(stop - before_sort_start))
    print("Search time: {:.2f}s".format(stop - after_sort_start))
    print("Counted: {}\n".format(len(found_records)))
