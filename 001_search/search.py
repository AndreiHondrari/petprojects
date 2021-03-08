
import sys
import pickle
import time
import random
from hashlib import sha1

from collections import defaultdict

from record import Record

from typing import List, Any

print(
    "Purpose of script: search thorugh multiple data instances and "
    "compare simple search versus smart search (including index search)"
)

# LOAD COLLECTIONS

start = time.time()
try:
    pf = open("data", "rb")
except FileNotFoundError as e:
    print(e)
    sys.exit()

collection = pickle.loads(pf.read())
pf.close()
print("Loading time: {:.2f}s".format(time.time() - start))
print("Length of collection to search: {}\n".format(len(collection)))

# SIMPLE SEARCHES
record_id = random.randint(0, len(collection))
search_record = collection[record_id]


print("#################################################################")
print("Simple search for short text: {}".format(search_record.short_text))
enumerated_collection = enumerate(collection)
count = 0
start = time.time()
for i, r in enumerated_collection:

    if i % 100000 == 0:
        print("Went through {} records.".format(i))

    if r.short_text == search_record.short_text:
        print("Found record: {}".format(r))
        count += 1

print("Search time: {:.2f}s".format(time.time() - start))
print("Counted: {}\n".format(count))

print("#################################################################")
print("Simple search for large text: {}".format(search_record.large_text))
enumerated_collection = enumerate(collection)
count = 0
start = time.time()
for i, r in enumerated_collection:

    if i % 100000 == 0:
        print("Went through {} records.".format(i))

    if r.large_text == search_record.large_text:
        print("Found record: {}".format(r))
        count += 1

print("Search time: {:.2f}s\n".format(time.time() - start))
print("Counted: {}\n".format(count))


# DIVIDE ET IMPERA SEARCH
def find_records(
    collection: List,
    attribute,
    value,
    inner=False
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
    collection = sorted(collection, key=lambda x: getattr(x, attribute))
    return find_records(collection, attribute, value)


print("#################################################################")
print(
    "Divide et impera search for short text "
    "(for post-sorted collection): {}".format(search_record.short_text)
)
start = time.time()
found_records = sort_and_find_records(
    collection, "short_text", search_record.short_text
)

for r in found_records:
    print("Found record: {}".format(r))

print("Search time: {:.2f}s".format(time.time() - start))
print("Counted: {}\n".format(len(found_records)))


print("#################################################################")
print("Divide et impera search for short text (for pre-sorted collection): {}".format(search_record.short_text))

sorted_collection = sorted(collection, key=lambda x: getattr(x, "short_text"))

start = time.time()
found_records = find_records(sorted_collection, "short_text", search_record.short_text)

for r in found_records:
    print("Found record: {}".format(r))

print("Search time: {:.2f}s".format(time.time() - start))
print("Counted: {}\n".format(len(found_records)))

print("#################################################################")
print("Divide et impera search for large text (for post-sorted collection): {}".format(search_record.large_text))
start = time.time()
found_records = sort_and_find_records(collection, "large_text", search_record.large_text)

for r in found_records:
    print("Found record: {}".format(r))

print("Search time: {:.2f}s".format(time.time() - start))
print("Counted: {}\n".format(len(found_records)))


print("#################################################################")
print("Divide et impera search for large text (for pre-sorted collection): {}".format(search_record.large_text))

sorted_collection = sorted(collection, key=lambda x: getattr(x, "large_text"))

start = time.time()
found_records = find_records(sorted_collection, "large_text", search_record.large_text)

for r in found_records:
    print("Found record: {}".format(r))

print("Search time: {:.2f}s".format(time.time() - start))
print("Counted: {}\n".format(len(found_records)))


# INDEXED SEARCH

# make the collection a dict for easy access by ID

print("################################################################")
print("Index searches")
print("Create indexes ...")
collection = {r.id: r for r in collection}


def index_code(value: Any) -> int:
    sha_obj = sha1(str(value).encode())
    return int(sha_obj.hexdigest(), 16)


def create_index(collection: List[Record], attribute: str) -> None:

    index = defaultdict(list)

    for i, r in collection.items():
        index[index_code(getattr(r, attribute))].append(r.id)

    return index

start = time.time()
short_text_index = create_index(collection, "short_text")
large_text_index = create_index(collection, "large_text")
print("Indexes build time: {:.2f}s\n".format(time.time() - start))

print("#################################################################")
print("Index search for short text (for indexed collection): {}".format(search_record.short_text))

start = time.time()

count = 0
search_code = index_code(search_record.short_text)
if search_code in short_text_index:
    for record_id in short_text_index[search_code]:
        print("Found record: {}".format(collection[record_id]))
        count += 1

print("Search time: {:.6f}s".format(time.time() - start))
print("Counted: {}\n".format(count))

print("#################################################################")
print("Index search for large text (for indexed collection): {}".format(search_record.large_text))

start = time.time()

search_code = index_code(search_record.large_text)
count = 0
if search_code in large_text_index:
    for record_id in large_text_index[search_code]:
        print("Found record: {}".format(collection[record_id]))
        count += 1

print("Search time: {:.6f}s".format(time.time() - start))
print("Counted: {}\n".format(count))
