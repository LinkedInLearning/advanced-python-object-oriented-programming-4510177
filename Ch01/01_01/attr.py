# %% Emulate build-in "getattr"
def find_attribute(obj, attr):
    if attr in obj.__dict__:
        print(f'found {attr} in instance')
        return obj.__dict__[attr]

    if attr in obj.__class__.__dict__:
        print(f'found {attr} in class')
        return obj.__class__.__dict__[attr]

    for cls in obj.__class__.__mro__:
        if attr not in cls.__dict__:
            continue
        print(f'found {attr} in parent {cls.__name__!r}')
        return cls.__dict__[attr]

    # TODO: __getattr__, descriptors ...

    raise AttributeError(attr)


# %% VM
class VM:
    version = '1.2.3'  # Class attribute.


class A1(VM):
    cpu_family = 'arm64'

    def __init__(self, id):
        self.id = id  # Instance attribute.
        self.state = 'running'

    def shutdown(self):
        # TODO
        self.state = 'stopped'


a1 = A1('9e99929')

#%% a1.id
print(find_attribute(a1, 'id'))

#%% a1.cpu_family
print(find_attribute(a1, 'cpu_family'))

#%% a1.version
print(find_attribute(a1, 'version'))

#%% a1.nic
print(find_attribute(a1, 'nic'))