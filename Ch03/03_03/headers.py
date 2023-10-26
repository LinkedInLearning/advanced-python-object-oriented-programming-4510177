# %% Headers
from collections.abc import Mapping

class Headers(Mapping):
    def __init__(self, headers: dict):
        self._headers = {
            key.lower(): value
            for key, value in headers.items()
        }

    def __len__(self):
        return len(self._headers)

    def __getitem__(self, key):
        key = key.lower()
        return self._headers[key]

    def __iter__(self):
        return iter(self._headers)


# %% Test
headers = Headers({
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': '1366',
    'Accept-Ranges': 'bytes',
})
print(len(headers), 'headers')
print('Content Type:', headers['content-type'])
for key in headers:
    print('key:', key)
for key, value in headers.items():
    print(key, '->', value)
