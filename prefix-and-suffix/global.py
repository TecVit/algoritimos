from math import gcd

def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    # soma[l..r] = prefix[r+1] - prefix[l]
    return prefix

def suffix_sum(arr):
    n = len(arr)
    suffix = [0]*(n+1)
    
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]

    # soma[l..r] = suffix[l] - suffix[r+1]
    return suffix

def prefix_gcd(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = gcd(prefix[i-1], arr[i])

    return prefix

def suffix_gcd(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[n-1] = arr[n-1]

    for i in range(n-2, -1, -1):
        suffix[i] = gcd(suffix[i+1], arr[i])
    return suffix