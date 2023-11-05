# %% serializer
serializers = {}  # media_type -> class


class serializer:
    def __init__(self, media_type):
        self.media_type = media_type
    
    def __call__(self, cls):
        if (other := serializers.get(self.media_type)):
            name = other.__name__
            msg = f'{self.media_type} already registered to {name}'
            raise ValueError(msg)
        
        dump = getattr(cls, 'dump', None)
        if not callable(dump):
            name = cls.__name__
            raise ValueError(f'{name} does not have a "dump" method')
        
        serializers[self.media_type] = cls
        return cls

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
