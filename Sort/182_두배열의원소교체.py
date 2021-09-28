# thisisCote implementation_두배열의원소교체 p.182

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우에만
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:  # 아닐 때는 안 바꿈
        break

print(sum(a))
