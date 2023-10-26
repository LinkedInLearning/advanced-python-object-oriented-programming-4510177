# %% Event
from dataclasses import dataclass

@dataclass
class Event:
    uri: str
    action: str


events = [
    Event(uri='file:///etc/passwd', action='READ'),
    Event(uri='file:///etc/passwd', action='WRITE'),
    Event(uri='file:///var/log/httpd', action='WRITE'),
    Event(uri='file:///etc/passwd', action='READ'),
]

# %% count
from collections import Counter

counts = Counter()
for evt in events:
    counts[evt] += 1
print(counts)