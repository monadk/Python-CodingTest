# 오답... ^^

m, n = map(int, input().split())
k = int(input())
stores = []
for _ in range(k):
    stores.append(tuple(map(int, input().split())))
loc = tuple(map(int, input().split()))

total = 0
for store in stores:
    if abs(store[0]-loc[0]) == 2:  # 마주보는 방향
        if store[0] // 2 == 0:  # 동/서쪽이면
            total += min(loc[1]+store[1]+m, n*2-loc[1]-store[1]+m)
        else:  # 남/북쪽
            total += min(loc[1]+store[1]+n, m*2-loc[1]-store[1]+n)
    elif store[0] == loc[0]:  # 같은 방향
        total += abs(loc[1]-store[1])
    else:  # 90도 방향
        if {store[0], loc[0]} == {1, 4}:
            if store[0] == 1:
                total += m-store[1]+loc[1]
            else:
                total += m-loc[1]+store[1]
        elif {store[0], loc[0]} == {1, 2}:
            total += store[1]+loc[1]
        elif {store[0], loc[0]} == {3, 4}:
            total += m+n-store[1]-loc[1]
        elif {store[0], loc[0]} == {2, 3}:
            if store[0] == 2:
                total += n-store[1]+loc[1]
            else:
                total += n-loc[1]+store[1]

print(total)
