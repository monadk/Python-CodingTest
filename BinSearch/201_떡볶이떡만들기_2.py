# thisisCote greedy_떡볶이떡만들기 p.201
# 내가 한 풀이
# 틀린 풀이이다. 왜냐하면 내 코드는 정확히 m값이 도출되지 않는다면
# 무한 루프에 빠지기 때문.
# 만일 나머지떡의 길이가 m보다 큰 경우, 이를 기록하는 장치가 있어야 함

n,m = map(int,input().split())
tteoks = list(map(int,input().split()))

def h_search(arr, start, end):
  global m
  if start > end:
    return None

  h = (start+end)//2
  sum_of_tteok = sum(map(lambda x: x-h if x>=h else 0, arr))
  
  if sum_of_tteok < m:
    return h_search(arr, start, h-1)
  elif sum_of_tteok == m:
    return h
  elif sum_of_tteok > m:
    return h_search(arr,h+1, end)

print(h_search(tteoks, 0, max(tteoks)))