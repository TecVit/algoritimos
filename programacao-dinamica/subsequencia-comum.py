# Subsequência Comum Máxima
def lcs(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

  for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
      if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])

  return dp[n1][n2]

def main():
  s1, s2 = map(str, input().split())
  print(lcs(s1, s2))

  return 0

if __name__ == "__main__":
  main()