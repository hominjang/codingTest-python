from collections import deque

a = deque()
a.append(5)
print(a)

a.append(2)
print(a)

a.append(3)
print(a)

a.append(7)
print(a)

a.popleft()
print(a)
a.append(1)
print(a)
a.append(4)
print(a)
a.popleft()

print(a)
