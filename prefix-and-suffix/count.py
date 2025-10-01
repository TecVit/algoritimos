def prefix_count(s):
  n = len(s)
  pref = [[0]*(n+1) for _ in range(26)]

  for i in range(n):
    for c in range(26):
      pref[c][i+1] = pref[c][i]
    pref[ord(s[i])-97][i+1] += 1

  return pref

# consulta: quantos 'a' existem entre [l,r]
# count = pref['a'][r+1] - pref['a'][l]

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

def dp_prefix(n, k):
  dp = [0]*(n+1)
  pref = [0]*(n+1)
  dp[0] = 1
  pref[1] = 1

  for i in range(1,n+1):
    dp[i] = pref[i] - (pref[i-k] if i-k>=0 else 0)
    pref[i+1] = pref[i] + dp[i]

  return dp[n]