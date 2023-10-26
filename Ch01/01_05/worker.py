# %% Worker
from datetime import datetime, timedelta
from time import time, sleep


class Worker:
    def __init__(self, id):
        self.id = id
        self._started = time()

    def uptime(self):
        return time() - self._started


# %% SpotWorker
class SpotWorker(Worker):
    def __init__(self, id):
        super().__init__(id)
        self._started = datetime.now()

    def cost(self):
        duration = datetime.now() - self._started
        return duration / timedelta(seconds=60) * 0.02

# %% Test
worker = SpotWorker('769f984')
sleep(0.123)
print(f'uptime: {worker.uptime():.2f}')
