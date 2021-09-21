# thisisCote greedy_거스름돈 p.87

money = int(input()) # 받은 돈
cnt = 0 # 거슬러줄 동전 개수
coin_type = [500, 100, 50, 10] # 큰 순서대로 정렬
#앞의 동전이 뒤의 동전보다 배수이므로 그리디 알고리즘 적합

for coin in coin_type:
  cnt += money // coin
  money %= coin

print (cnt)
