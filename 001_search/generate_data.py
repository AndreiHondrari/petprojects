
import pickle
import time
import random

import faker  # type: ignore[import]

from record import Record, RecordPlaceholder

from typing import List

finst = faker.Faker()

print(
    "Purpose of script: generate many data records"
)

print("Generate data...")

start = time.time()

placeholders: List[RecordPlaceholder] = []

NO_OF_ITEMS = 500000

for i in range(NO_OF_ITEMS):

    if i % 10000 == 0:
        print("Generated {} data items.".format(i))

    placeholders.append(
        RecordPlaceholder(
            finst.text(max_nb_chars=20),
            finst.text(),
            random.randint(0, 10000)
        )
    )

some_placholders1 = placeholders[0:len(placeholders) // 2]
some_placholders2 = placeholders[len(placeholders) // 2:]

placeholders.extend(some_placholders1)

# triplicate half of the original set of record placeholders
placeholders.extend(some_placholders2 * 3)

print("Shuffling ...")
random.shuffle(placeholders)

print("Generating collection with id's ...")
collection = []

for i, pholder in enumerate(placeholders):
    collection.append(
        Record(i, pholder.short_text, pholder.large_text, pholder.number)
    )

print("Generation time: {:.2f}s".format(time.time() - start))
print("Length of collection: {}\n".format(len(collection)))

print("Write to file ...")
pf = open("data", "wb")
pf.write(pickle.dumps(collection))
pf.close()

print("DONE!")
