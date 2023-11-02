# %% Stack
from collections.abc import Sequence

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack(Sequence):
    def __init__(self):
        self._head = None

    def push(self, value):
        self._head = Node(value, self._head)

    def pop(self):
        if self._head is None:
            raise ValueError('pop from empty stack')

        value = self._head.value
        self._head = self._head.next
        return value

    def __len__(self):
        count = 0
        node = self._head
        while node:
            count += 1
            node = node.next
        return count

    def __getitem__(self, index):
        node = self._head
        while index > 0 and node:
            index -= 1
            node = node.next
        if not node:
            raise IndexError(index)
        return node.value



# %% Test
s = Stack()
for c in 'Python':
    s.push(c)
print('len:', len(s))
print('s[2]:', s[2])
print('t' in s)
