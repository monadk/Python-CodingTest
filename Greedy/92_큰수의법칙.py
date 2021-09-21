# thisisCote greedy_큰수의법칙 p.92

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# 가장 큰수와 두번째로 큰수를 찾으면 된다
nums.sort(reverse=True)
first = nums[0]
second = nums[1]

result = 0  
# 최대값*k+두번째값이 m//k+1만큼 반복되어 더해질 수 있음
result += m//(k+1) * (first*k+second)
result += m%(k+1) * first

print(result)


# review
# 큰수가 더해지는 횟수를 cnt 변수로 저장했으면 코드가 더 깔끔했을 듯.
# cnt = m//(k+1)*k + m%(k+1)