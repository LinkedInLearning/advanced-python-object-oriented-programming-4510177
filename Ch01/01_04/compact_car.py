# %% Car
class Car:
    __slots__ = ['id', 'lat', 'lng']

    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat
        self.lng = lng


# %% Memory
import tracemalloc
from random import random

def rand_lat():
    return random()*180 - 90

def rand_lng():
    return random()*360 - 180

def mb(bytes):
    return bytes/1_000_000

size = 100_000

tracemalloc.start()
cars = [Car(i, rand_lat(), rand_lng()) for i in range(size)]
current, peak = tracemalloc.get_traced_memory()
print('current:', mb(current), 'peak:', mb(peak))