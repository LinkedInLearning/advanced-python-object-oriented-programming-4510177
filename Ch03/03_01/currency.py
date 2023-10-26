# %% Payment
import re


class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f'{self.amount:.2f}{self.currency}'

    def __repr__(self):
        name = self.__class__.__name__  # Support inheritance.
        return f'{name}({self.amount!r}, {self.currency!r})'

    def _replace(self, match):
        if match[1] == 'a':
            return f'{self.amount:.2f}'
        if match[1] == 'c':
            return self.currency
        raise ValueError(f'unknown format: {match.group()}')

    def __format__(self, spec):
        return re.sub(r'(?<!%)%([ac])', self._replace, spec)



p = Payment(123.45, '£')

# %% str
print(f'payment of {p}')

# %% repr
print(f'p={p!r}')
print(f'{p=}')

# %% format
print(f'A payment of {p:%a} in {p:%c}')
