
import time

from typing import List

from record import Record


def simple_search_short_text(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Simple search for short text: {}\n".format(target_record.short_text)
    )
    enumerated_collection = enumerate(collection)
    count = 0
    start = time.time()
    for i, r in enumerated_collection:

        if i % 100000 == 0:
            print("Went through {} records.".format(i))

        if r.short_text == target_record.short_text:
            print("Found record: {}".format(r.id))
            count += 1

    print("\nSearch time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(count))


def simple_search_long_text(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Simple search for large text: {}\n".format(target_record.large_text)
    )
    enumerated_collection = enumerate(collection)
    count = 0
    start = time.time()
    for i, r in enumerated_collection:

        if i % 100000 == 0:
            print("Went through {} records.".format(i))

        if r.large_text == target_record.large_text:
            print("Found record: {}".format(r.id))
            count += 1

    print("\nSearch time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(count))
