
import time

from typing import List

from record import Record
from search_tools.divide_et_impera import find_records, sort_and_find_records


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
            print("\nFound record: {}\n".format(r))
            count += 1

    print("Search time: {:.2f}s".format(time.time() - start))
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
            print("\nFound record: {}\n".format(r))
            count += 1

    print("Search time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(count))


def postsorted_search_short_text(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Divide et impera search for short text "
        "(for post-sorted collection): {}\n".format(target_record.short_text)
    )
    start = time.time()
    found_records = sort_and_find_records(
        collection, "short_text", target_record.short_text
    )

    for r in found_records:
        print("Found record: {}\n".format(r))

    print("Search time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(len(found_records)))


def presorted_search_short_text(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Divide et impera search for short text "
        "(for pre-sorted collection): {}\n".format(target_record.short_text)
    )

    sorted_collection = sorted(
        collection,
        key=lambda x: getattr(x, "short_text")  # type: ignore[no-any-return]
    )

    start = time.time()
    found_records = find_records(
        sorted_collection,
        "short_text",
        target_record.short_text
    )

    for r in found_records:
        print("Found record: {}\n".format(r))

    print("Search time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(len(found_records)))


def postsorted_search_long_text(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Divide et impera search for large text "
        "(for post-sorted collection): {}\n".format(target_record.large_text)
    )
    start = time.time()
    found_records = sort_and_find_records(
        collection,
        "large_text",
        target_record.large_text
    )

    for r in found_records:
        print("Found record: {}\n".format(r))

    print("Search time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(len(found_records)))


def presorted_search_long_text(
    target_record: Record,
    collection: List[Record]
) -> None:
    print("#################################################################")
    print(
        "Divide et impera search for large text "
        "(for pre-sorted collection): {}\n".format(target_record.large_text)
    )

    sorted_collection = sorted(
        collection,
        key=lambda x: getattr(x, "large_text")  # type: ignore[no-any-return]
    )

    start = time.time()
    found_records = find_records(
        sorted_collection,
        "large_text",
        target_record.large_text
    )

    for r in found_records:
        print("Found record: {}\n".format(r))

    print("Search time: {:.2f}s".format(time.time() - start))
    print("Counted: {}\n".format(len(found_records)))
