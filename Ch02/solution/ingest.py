# %% Events
class LoginEvent:
    def __init__(self, login):
        self.login = login

    def notify_loaded(self):
        print('LoginEvent loaded')


class AccessEvent:
    def __init__(self, login, uri):
        self.login = login
        self.uri = uri

    def notify_loaded(self):
        print(f'AccessEvent loaded (uri={self.uri!r})')


# Add an ability to load events from JSON data (str)
# Use a Mixin class
# Make sure that Events have notify_loaded method (ABC)


# %% Serialized
from abc import ABC, abstractmethod
import json

class Serialized(ABC):
    @classmethod
    def from_json(cls, data):
        params = json.loads(data)
        inst = cls(**params)
        inst.notify_loaded()
        return inst

    @abstractmethod
    def notify_loaded(self):
        pass


# %% MixIns
class SerializeLogin(LoginEvent, Serialized):
    pass

class SerializedAccess(AccessEvent, Serialized):
    pass


# %% Test
# LoginEvent
login_data = '{"login": "elliot"}'
# AccessEvent
access_data = '''
{
  "login": "elliot",
  "uri": "file:///etc/passwd"
}
'''

event = SerializeLogin.from_json(login_data)
event = SerializedAccess.from_json(access_data)
