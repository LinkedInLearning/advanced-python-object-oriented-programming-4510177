# %% Player
class Player:
    num_players = 0  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute
        self.mana = 100
        self.num_players += 1
        print('self:', self.num_players)


# %% Test
p1 = Player('Parzival')
print('Player:', Player.num_players)