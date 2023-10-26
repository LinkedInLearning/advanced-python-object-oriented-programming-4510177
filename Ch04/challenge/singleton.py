# %% Singleton
class Singleton:
    # TODO
    pass


# %% Test

class Driver(Singleton):
    pass

d1 = Driver()
d2 = Driver()
print(d1 is d2)
