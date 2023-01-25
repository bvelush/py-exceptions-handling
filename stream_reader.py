from typing import List


def stream_reader(name: str) -> List[str]:
    with open(name, 'rt') as f:
        yield f.readline()
