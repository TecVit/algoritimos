def main():
  n = int(input())
  
  if (n <= 1):
    print(n)
    return
  
  dp = [-1] * (n + 1)
  dp[0] = 0
  dp[1] = 1

  for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

  print(dp[n])

  return 0

if __name__ == "__main__":
  main()