
import pickle
import time
import random

import faker

from record import Record

finst = faker.Faker()

print(
    "Purpose of script: generate many data records"
)

print("Generate data...")

start = time.time()
collection = [
    Record(
        id=i, 
        short_text=finst.text(max_nb_chars=20), 
        large_text=finst.text(), 
        number=random.randint(0, 10000)
    )
    for i in range(500000)
]

some_col1 = collection[0:len(collection) // 2]
some_col2 = collection[len(collection) // 2:]

collection.extend(some_col1)
collection.extend(some_col2 * 3)

print("Shuffling ...")
random.shuffle(collection)

print("Generation time: {:.2f}s".format(time.time() - start))
print("Length of collection: {}\n".format(len(collection)))

print("Write to file ...")
pf = open("data", "wb")
pf.write(pickle.dumps(collection))
pf.close()

print("DONE!")
