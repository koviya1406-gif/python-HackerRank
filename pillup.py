
from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    command, *args = input().split()
    getattr(d, command)(*args)
print(*d)
