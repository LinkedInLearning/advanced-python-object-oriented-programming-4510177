# %% Duration

class Duration:
    unit_values = {
        'ns': 1,
        'us': 1000,
        'ms': 1_000_000,
    }

    def __init__(self, value: float, unit: str):
        if value < 0 or unit not in Duration.unit_values:
            raise ValueError(f'invalid duration: {value=}, {unit=}')

        self.value = value
        self.unit = unit

    def __repr__(self):
        return f'{self.value}{self.unit}'

    def __add__(self, other):
        v1 = self.value * Duration.unit_values[self.unit]
        v2 = other.value * Duration.unit_values[other.unit]
        value = (v1 + v2) / Duration.unit_values[self.unit]
        return Duration(value, self.unit)


# %% Test
u1 = Duration(317, 'us')
u2 = Duration(2.7, 'ms')
print(u1 + u2)
