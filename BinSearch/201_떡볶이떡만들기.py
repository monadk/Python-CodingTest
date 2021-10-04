# thisisCote greedy_떡볶이떡만들기 p.201

n, m = map(int, input().split())
tteoks = list(map(int, input().split()))

start = 0
end = max(tteoks)

result = 0
while (start <= end):
    h = (start+end) // 2
    # h만큼 잘랐을 때 나머지 떡의 길이
    total = sum(map(lambda x: x-h if x > h else 0, tteoks))

    if total < m:  # 떡이 모자라므로 h를 줄여야 함
        end = h - 1
        continue
    else:  # 떡이 m의 길이는 보장하나, 최대의 h값을 찾기 위해 더 탐색해봐야 함
        result = h  # 최대한 덜 잘랐을 때가 정답이므로, result 기록 **************
        start = h + 1

print(result)
