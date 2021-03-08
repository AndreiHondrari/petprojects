
import sys
import pickle
import time
import random

from typing import List, Dict

from record import Record
from search_tools.indexed import create_index
from search_procedures import (
    linear as linear_procedures,
    divide_et_impera as dei_procedures,
    indexed as idx_procedures,
)


if __name__ == "__main__":
    print(
        "Purpose of script: search thorugh multiple data instances and "
        "compare simple search versus smart search (including index search)"
    )

    # LOAD COLLECTION
    start = time.time()
    try:
        pf = open("data", "rb")
    except FileNotFoundError as e:
        print(e)
        sys.exit()

    COLLECTION: List[Record] = pickle.loads(pf.read())
    pf.close()
    print("Loading time: {:.2f}s".format(time.time() - start))
    print("Length of collection to search: {}\n".format(len(COLLECTION)))

    # GET RANDOM SEARCH TARGET
    record_index = random.randint(0, len(COLLECTION))
    target_record = COLLECTION[record_index]

    # LINEAR SEARCH
    print("################################################################")
    print("Linear search\n")
    linear_procedures.simple_search_short_text(target_record, COLLECTION)
    linear_procedures.simple_search_long_text(target_record, COLLECTION)

    # DIVIDE ET IMPERA SEARCH
    print("################################################################")
    print("Divide et impera search\n")
    dei_procedures.search_short_text_in_sorted_collection(
        target_record, COLLECTION
    )
    dei_procedures.search_long_text_in_sorted_collection(
        target_record, COLLECTION
    )

    # INDEXED SEARCH

    # make the collection a dict for easy access by ID
    print("################################################################")
    print("Index search\n")

    print("Create indexes ...")
    IDENTIFIED_COLLECTION: Dict[int, Record] = {r.id: r for r in COLLECTION}

    start = time.time()
    short_text_index: Dict[int, List[int]] = create_index(
        IDENTIFIED_COLLECTION,
        "short_text"
    )
    large_text_index: Dict[int, List[int]] = create_index(
        IDENTIFIED_COLLECTION,
        "large_text"
    )
    print("Indexes build time: {:.2f}s\n".format(time.time() - start))

    idx_procedures.search_short_text(
        target_record,
        IDENTIFIED_COLLECTION,
        short_text_index
    )

    idx_procedures.search_long_text(
        target_record,
        IDENTIFIED_COLLECTION,
        large_text_index
    )
