# %% serializer
serializers = {}  # media_type -> class


def serializer(media_type):
    def decorator(cls):
        if (other := serializers.get(media_type)):
            msg = f'{media_type} already registered to {other.__name__}'
            raise ValueError(msg)

        dump = getattr(cls, 'dump', None)
        if not callable(dump):
            raise ValueError(f'{cls.__name__} does not have a "dump" method')

        serializers[media_type] = cls
        return cls
    return decorator


def serialize(out, media_type, objects):
    cls = serializers.get(media_type)
    if cls is None:
        raise ValueError('unknown media type: {media_type!r}')
    serializer = cls(out)
    for obj in objects:
        serializer.dump(obj)


# %% JSON
import json


@serializer('application/json')
class JSONSerializer:
    def __init__(self, out):
        self.out = out

    def dump(self, obj):
        json.dump(obj, self.out)
        self.out.write('\n')

# %% Test
import sys

events = [
    {
        'login': 'elliot',
        'action': 'logout',
    },
    {
        'login': 'elliot',
        'action': 'access',
        'uri': 'file:///etc/passwd',
    },
]
serialize(sys.stdout, 'application/json', events)
