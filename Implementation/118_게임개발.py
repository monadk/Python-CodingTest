# thisisCote implementation_게임개발 p.118

# 시뮬레이션, 삼전 공채 코테에서 자주 출제
# 반복적 숙달이 필요한 유형임
# direction을 설정해서 이동하는 유형은 dx, dy리스트 만드는게 효과적

n,m = map(int,input().split())
a,b,d = map(int,input().split())
#a,b = a-1, b-1

gamemap = [] # 육지 0 바다 1
for i in range(n):
  gamemap.append(list(map(int,input().split())))
da = [-1,0,1,0]
db = [0,1,0,-1]

visited = [[0]*m for _ in range(n)]
visited[a][b] = 1

def turn_left():
  global d
  d -= 1
  if d < 0: d = 3

cnt = 1 # 방문한 칸의 수
turned_cnt = 0 # 회전한 횟수 (4가 되면 뒤로 감)
while True:
  # 아무튼 왼쪽은 도니까
  turn_left()
  # 다음칸 확인 - gamemap, visited
  na = a+da[d]
  nb = b+db[d]
  # 다음(왼쪽)칸이 외곽도 아니고, 바다도 아니고, 방문한 곳도 아닐 때
  if gamemap[na][nb] == 0 and visited[na][nb] == 0:
    # 이동, 방문표시, turned_cnt 초기화
    a = na
    b = nb
    visited[a][b] = 1
    cnt += 1
    turned_cnt = 0
    continue
  else: 
    turned_cnt += 1

  if turned_cnt == 4:
    na = a-da[d]
    nb = b-db[d]
    if gamemap[na][nb] == 0: 
      a = na
      b = nb
      turned_cnt = 0
    else:
      break

print(cnt)


# review
# 어렵다.. 다시 풀어보기..^^
# 변수는 문제내주는 그대로 사용하는 편이 좋을 듯함