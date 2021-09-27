# thisisCote greedy_미로탈출 p.152

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:  # 큐가 빌 때까지 반복
        cx, cy = q.popleft()

        for i in range(4):  # 상하좌우 탐색! (깊이 1단계씩)
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:  # 범위 벗어남
                continue
            if graph[nx][ny] == 0:  # 괴물 있는 곳이면
                continue
            if graph[nx][ny] == 1:  # 방문한 적이 없는 곳이면 +1 하여 최단거리 기록
                graph[nx][ny] = graph[cx][cy]+1
                q.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0, 0))

# bfs는 재귀 양상이 없다는 것을 꼭 기억하기
# bfs는 같은 깊이에 있는 노드를 우선 탐색하므로 (가까운 순서대로) 결국 최단 거리가 보장된다는 점..
