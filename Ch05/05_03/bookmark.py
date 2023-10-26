# %% Bookmark
from dataclasses import dataclass, field
from datetime import datetime, UTC

@dataclass
class Bookmark:
    url: str
    title: str = ''
    tags: list[str] = field(default_factory=list) 
    created: datetime = None


    def __post_init__(self):
        if self.created == None:
            self.created = datetime.now(tz=UTC)

b1 = Bookmark(
    url='https://fastapi.tiangolo.com/',
    title='FastAPI web framework',
    tags=['python', 'web', 'server'],
)
print(b1)

# %%
b2 = Bookmark(
    url='https://python.org',
)
b2.title = 'Python programming language'
print(b2)