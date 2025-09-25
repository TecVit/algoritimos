import bisect

n = int(input())
v = list(map(int, input().split()))

idx = bisect.bisect_left(v, n)
print(idx if idx < len(v) and v[idx] == 7 else -1)