# %% VM
from random import choice

adjectives = ['cool', 'funny', 'strong']
names = ['bruce', 'carol', 'natasha']


class VM:
    def __init__(self):
        self.name = VM.random_name()


    @staticmethod
    def random_name():
        adjective, name = choice(adjectives), choice(names)
        return f'{adjective}_{name}'


# %% Test
vm = VM()
print(vm.name)
