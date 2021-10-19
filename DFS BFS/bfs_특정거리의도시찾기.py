from collections import deque

n, m, k, x = map(int, input().split())
roads = []
for _ in range(m):
    roads.append(tuple(map(int, input().split())))

cities = [0]*(n+1)


def bfs(start):
    # blabla
    q = deque(start)


bfs(x)

print(i for i in range(1, n+1) if cities(i) == k)
