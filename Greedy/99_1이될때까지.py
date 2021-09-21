# thisisCote greedy_1이 될 때까지 p.99

# 최대한 많이 나누기 수행. bc 나누는 횟수가 1씩 빼는 횟수보다 항상 작음

n, k = map(int, input().split())
cnt = 0
while True:  # 나누기 위한 While 문
  cnt += n%k 
  n -= (n%k) # 나누어 떨어질때까지 1빼기
  if n<k:  # n을 k로 나눌수 없을 때 나가기
    break
  n //= k
  cnt += 1

cnt += (n-1)  # 마지막으로 남은 수 빼주기
print(cnt)

# review
# 한번 더 풀어보기...^^
# 웬만하면 입력받았던 변수를 최대한 변질시키지 않으려 노력하기