# thisisCote implementation_위에서아래로 p.178

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')
