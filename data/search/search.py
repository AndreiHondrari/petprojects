
import sys
import pickle
import time
import random

from record import Record

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


def find_records(collection, attribute, value, inner=False):

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


def sort_and_find_records(collection, attribute, value):
    collection = sorted(collection, key=lambda x: getattr(x, attribute))
    return find_records(collection, attribute, value)
    

print("#################################################################")
print("Divide et impera search for short text (for post-sorted collection): {}".format(search_record.short_text))
start = time.time()
found_records = sort_and_find_records(collection, "short_text", search_record.short_text)

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
