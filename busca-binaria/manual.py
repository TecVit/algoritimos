# import bisect
# n = int(input())
# v = list(map(int, input().split()))

# idx = bisect.bisect_left(v, n)
# print(idx if idx < len(v) and v[idx] == 7 else -1)

def busca_binaria(arr, alvo):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
    if arr[mid] == alvo:
        return mid
    elif arr[mid] < alvo:
        l = mid + 1
    else:
        r = mid - 1
        
    return -1