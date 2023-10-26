# %% Validator
class Validator:
    attr_name = '_validators'

    def __set_name__(self, cls, name):
        print(f'__set_name__: {name=}')
        validator_name = self.__class__.__name__
        self._key = f'{validator_name}_{name}'

    def __get__(self, inst, cls):
        print(f'__get__: {inst=}, {cls=}')
        if inst is None:  # Access via class.
            return self

        values = getattr(inst, Validator.attr_name, {})
        return values.get(self._key)

    def __set__(self, inst, value):
        print(f'__set__: {inst=}, {value=}')
        self.validate(value)
        values = getattr(inst, Validator.attr_name, None)
        if values is None:
            values = {}
            setattr(inst, Validator.attr_name, values)
        values[self._key] = value

    def _get_values(self, inst):
        attr = '_validators'
        values = getattr(inst, attr, None)
        if inst is None:
            values = {}
            setattr(inst, attr, values)
        return values

    def validate(self, value):
        raise NotImplementedError()


# %% Price
class Price(Validator):
    def validate(self, value):
        if value <= 0:
            raise ValueError(f'negtaive price: {value!r}')

# %% Trade
class Trade:
    open = Price()
    close = Price()

    def __init__(self, open, close):
        self.open = open
        self.close = close
        

t1 = Trade(133.2, 147.5)
print(t1.__dict__)

# %% Getting
print(Trade.open)  # Class level.
print(t1.open)  # Instance level.

# %% Setting
t1.close = 147.2

# %% Error

t1.close = -2