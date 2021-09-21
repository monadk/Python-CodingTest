# thisisCote implementation_왕실의 나이트 p.115

# 완전 탐색 & 시뮬레이션?

position = input()
x = int(ord(position[0]))-int(ord('a')) + 1
y = int(position[1])

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

cnt = 0
for step in steps:
  nx = step[0]+x
  ny = step[1]+y
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  cnt += 1

print(cnt)

# review
# dx, dy리스트 대신 steps로 수행. 이 2가지 형태 모두 기억해두기