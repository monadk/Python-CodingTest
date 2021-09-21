# thisisCote implementation_상하좌우 p.110

# 시뮬레이션

n = int(input())
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
moves = ['L','R','U','D']

x,y = 1,1
for plan in plans:
  idx = moves.index(plan)
  nx = x + dx[idx]
  ny = y + dy[idx]
  if nx >=1 and nx <= n and ny >=1 and ny <= n:
    x, y = nx, ny

print(x, y)

# review
# 시뮬레이션의 경우 x, y 방향 잘 확인하기
# 방향에 대해서는 dx, dy와 같은 리스트를 각각 두는 게 좋음
# 가면 안되는 곳에 대한 확인을 위해 nx, ny와 같은 next step 판별용 변수를 두는 게 좋음
