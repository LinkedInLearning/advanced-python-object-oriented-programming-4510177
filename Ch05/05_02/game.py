# %% Room
from collections import namedtuple

Room = namedtuple('Room', 'x y')

r1 = Room(1, 2)
print(r1)
# %% Attributes
print('len:', len(r1))
print('x:', r1.x)
print('[0]:', r1[0])

# %% attributes
from collections import defaultdict

players = defaultdict(list)
players[r1].append('amy')
print(players)

# %% replace
r2 = r1._replace(x=3)
print(r2)

# %% asdict
print(r2._asdict())

# %% compare
Range = namedtuple('Range', 'low high')

rng = Range(1, 2)
print(rng == r1)
