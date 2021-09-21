# thisisCote implementation_시각 p.113

# 완전탐색 : 탐색해야 할 전체데이터 개수가 100만개 이하일 때 완전 탐색 이용

n = int(input())

cnt = 0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h)+str(m)+str(s):
        cnt += 1

print(cnt)

# review
# range를 잘 확인하기