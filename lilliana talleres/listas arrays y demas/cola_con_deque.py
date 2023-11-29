from collections import deque

cola = deque()

cola.append(2)
cola.append(6)
cola.append(23)

print(cola)

cola.popleft()

print(cola)