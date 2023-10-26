# %% Singleton
class SingletonMeta(type):
    def __call__(cls, *args, **kw):
        inst = getattr(cls, '_instance', None)
        if inst is None:
            inst = cls._instance = type.__call__(cls, *args, **kw)
        return inst


class Singleton(metaclass=SingletonMeta):
    pass


# %% Test

class Driver(Singleton):
    pass

d1 = Driver()
d2 = Driver()
print(d1 is d2)
