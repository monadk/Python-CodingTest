# thisisCote greedy_숫자 카드 게임 p.96

# 각 행마다 가장 작은 수를 찾은 뒤, 그 중에서 가장 큰 수 찾기
n, m = map(int, input().split())
min_cards = []
for i in range(n):
  min_cards.append(min(list(map(int, input().split()))))

print(max(min_cards))

# review
# min_cards라는 배열 없이도 for문 내에서 max값을 찾을 수 있음
# (for문 안) result = max(result,min(list(map(int, input().split()))))