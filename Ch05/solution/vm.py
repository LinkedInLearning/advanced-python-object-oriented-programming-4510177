"""
Use a dataclass, write a VM class that has the following fields:
- id: str, no default
- cpus: int, default to 2
- memory: int, default to 512 (in MB)
- state: one of 'starting', 'running', 'stopped'
- tags: list of str, default to empty

After the VM is created, check that
- id is not empty
- cpus >= 1
- memory >= 256
"""
# %% VM
from dataclasses import dataclass, field

@dataclass
class VM:
    id: str
    cpus: int = 2
    memory: int = 512  # MB
    state: str = 'starting'
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            raise ValueError('empty ID')
        if self.cpus < 1:
            raise ValueError(f'cpus (self.cpus) < 1')
        if self.memory < 256:
            raise ValueError(f'memory (self.memory) < 256')

# %% test
vm = VM(
    id='i-0af01c0123456789a',
    cpus=4,
    memory=2048,
    tags=['db', 'env:qa']
)
print(vm)
