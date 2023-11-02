# %% Logger
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
)

class LoggerMixin:
    def log_id(self):
        logging.info('%s with id %r', self.name, self.id)


# %% User
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# %% VM
class VM:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# %% Mixing
class LoggedUser(LoggerMixin, User):
    pass

class LoggedVM(LoggerMixin, VM):
    pass


# %% Test
user = LoggedUser('root', 1)
user.log_id()

vm = LoggedVM('m1', '4922a77')
vm.log_id()
