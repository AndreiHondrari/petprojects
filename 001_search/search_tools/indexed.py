
from collections import defaultdict
from hashlib import sha1
from typing import Any, List, Dict

from record import Record


def index_code(value: Any) -> int:
    sha_obj = sha1(str(value).encode())
    return int(sha_obj.hexdigest(), 16)


def create_index(
    collection: Dict[int, Record],
    attribute: str,
) -> Dict[int, List[int]]:

    index: Dict[int, List[int]] = defaultdict(list)

    for i, r in collection.items():
        index[
            index_code(getattr(r, attribute))
        ].append(r.id)

    return index
