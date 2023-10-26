# %% normalize
def normalize(value):
    return value * .9


# %% Norm
class Norm:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value


# %% Test
n93 = Norm(.93)
print(n93(100))

# %%
def make_norm(factor):
    return lambda value: factor * value

n93 = make_norm(.93)
print(n93(100))
