# %% Writer
from typing import Protocol


class Writer(Protocol):
    def write(self, data: bytes) -> None:
        ...


# %% Store 
import json

def store_json(w: Writer, obj: dict) -> None:
    data = json.dumps(obj).encode('utf-8')
    w.write(data)


# %% S3File
class S3File:
    def write(self, data: str) -> None:
        # TODO
        print(f's3: write: {data!r}')


# %% Test
sink = S3File()
obj = {
    'id': '007',
    'lat': 51.4871871,
    'lng': -0.1270605,
}
store_json(sink, obj)
