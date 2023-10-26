# %% Robot
class Robot:
    manufacture = 'BnL'

    def move(self, x, y):
        print(f'{self} moving to {x}/{y}')


walle = Robot()
walle.move(100, 200)


# %% What "class" keyword does
from textwrap import dedent

class_body = '''
    manufacture = 'BnL'

    def move(self, x, y):
        print(f'{self} moving to {x}/{y}')
'''

cls_dict = {}
exec(dedent(class_body), None, cls_dict)
print(cls_dict)
move = cls_dict['move']
print(move.__code__.co_varnames)
move(walle, 10, 20)

# %% Using type
Robot = type(
    'Robot',
    (object,),
    cls_dict,
)
walle = Robot()
walle.move(100, 200)
