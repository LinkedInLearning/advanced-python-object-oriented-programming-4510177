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

# %% test
vm = VM(
    id='i-0af01c0123456789a',
    cpus=4,
    memory=2048,
    tags=['db', 'env:qa']
)
print(vm)