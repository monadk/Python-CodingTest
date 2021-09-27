# thisisCote greedy_음료수얼려먹기 p.149

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 갈 수 없는 곳이면 종료
    if graph[x][y] == 1:
        return False
    # 갈 수 있는 곳이면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 상하좌우 방문
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)


# 특정한 노드를 만났을 때 깊숙이 탐색하는 것이므로 dfs (상하좌우도 0인지 확인)
# visited 리스트가 굳이 필요하지 않은 케이스였다,,,
# 그래프가 0과 1로만 이루어졌으므로 이미 방문한 곳은 1로 업데이트해주면 되었음
