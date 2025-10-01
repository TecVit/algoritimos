def prefix_hash(s, base=131, mod=10**9+7):
  n = len(s)
  h = [0]*(n+1)
  p = [1]*(n+1)
  for i in range(n):
    h[i+1] = (h[i]*base + ord(s[i])) % mod
    p[i+1] = (p[i]*base) % mod
  return h, p

def get_hash(h, p, l, r, mod=10**9+7):
  return (h[r+1] - h[l]*p[r-l+1]) % mod

def max_common_substring(s1, s2):
  h1, p1 = prefix_hash(s1)
  h2, p2 = prefix_hash(s2)
  
  low, high = 0, min(len(s1), len(s2))
  ans = 0
  
  while low <= high:
    mid = (low + high)//2
    found = False
    hashes_s1 = set(get_hash(h1,p1,i,i+mid-1) for i in range(len(s1)-mid+1))
    for i in range(len(s2)-mid+1):
      if get_hash(h2,p2,i,i+mid-1) in hashes_s1:
        found = True
        break
    if found:
      ans = mid
      low = mid+1
    else:
      high = mid-1
  return ans