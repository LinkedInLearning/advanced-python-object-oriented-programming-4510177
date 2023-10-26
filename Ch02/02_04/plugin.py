# %% Plugins

class LoggingPlugin:
    def notify(self, event):
        print(f'got {event}')

    def shutdown(self):
        print('logger shutting down')


class SecurityPlugin:
    def notify(self, event):
        if event.action == 'login' and event.user == 'elliot':
            print(f'WARNING: {event.user} has logged in')

    def shutdwon(self):
        print('security shutting down')


def notify(plugins, event):
    for plugin in plugins:
        plugin.notify(event)


def shutdown(plugins):
    for plugin in plugins:
        plugin.shutdown()



# %% Test
class Event:
    def __init__(self, user, action):
        self.user = user
        self.action = action

plugins = [LoggingPlugin(), SecurityPlugin()]
event = Event('elliot', 'login')
notify(plugins, event)
shutdown(plugins)
