# thisisCote greedy_부품찾기 p.197

n = int(input())
store = list(map(int, input().split()))
store.sort()
m = int(input())
buying = list(map(int, input().split()))


def bin_search(tar, start, end, arr):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == tar:
        return mid
    elif arr[mid] < tar:
        return bin_search(tar, mid+1, end, arr)
    else:
        return bin_search(tar, start, mid-1, arr)


for i in range(m):
    if bin_search(buying[i], 0, n-1, store) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
