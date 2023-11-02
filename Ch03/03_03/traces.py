# %% Traces
class TraceIDs(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._counter = 1

    def __missing__(self, key):
        val = self._counter
        self._counter += 1
        self[key] = val
        return val


# %% Test
trace_ids = TraceIDs()
print('calls ID:', trace_ids['http.calls'])
print('calls ID:', trace_ids['http.calls'])
print('errors ID:', trace_ids['http.errors'])


# %%
from collections import defaultdict
from itertools import count

trace_ids = defaultdict(count(1).__next__)
print('calls ID:', trace_ids['http.calls'])
print('calls ID:', trace_ids['http.calls'])
print('errors ID:', trace_ids['http.errors'])
