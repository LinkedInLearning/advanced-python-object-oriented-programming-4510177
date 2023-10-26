# Methods of class creation
# __new__(mclas, name, bases, mapping) : Create new class
# __init__(*args, **kw)                : Initialize the class
# ... 

# %%
from datetime import datetime


class CheckerMeta(type):
    """
    If you have a procedure with 10 parameters, you probably missed some.
        - Alan J. Perlis
    """
    def __new__(mclass, name, bases, mapping):
        print(f'[checker] Creating class {name} with {bases}')
        mapping['created'] = datetime.now()
        return type.__new__(mclass, name, bases, mapping)

    def __init__(cls, name, bases, mapping):
        count = sum(1 for v in mapping.values() if callable(v))
        if count > 10:
            raise ValueError(f'{name} has too many methods ({count})')
        print(f'[checker] {name} with {count} methods')
        return type.__init__(cls, name, bases, mapping)

    def __call__(cls, *args, **kw):
        print(f'[checker] instance of {cls.__name__} created')
        if (count := len(args) + len(kw) > 10):
            name = cls.__name__
            raise ValueError(f'{name} instance with too many arguments ({count})')
        return type.__call__(cls, *args, **kw)


class Checker(metaclass=CheckerMeta):
    pass


class Robot(Checker):
    manufacture = 'BnL'

    def move(self, x, y):
        print(f'{self} moving to {x}/{y}')


walle = Robot()
walle.move(100, 200)
