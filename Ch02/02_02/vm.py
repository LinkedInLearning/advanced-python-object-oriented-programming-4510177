# VM
from random import choice

names = ['bruce', 'carol', 'natasha']
adjectives = ['cool', 'funny', 'strong']


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
