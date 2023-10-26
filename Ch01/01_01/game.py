# %% Player
class Player:
    num_players = 0

    def __init__(self, name):
        self.name = name
        self.mana = 100
        self.num_players += 1
        print('self:', self.num_players)


# %% Test
p1 = Player('Parzival')
print('Player:', Player.num_players)