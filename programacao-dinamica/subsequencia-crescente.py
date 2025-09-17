# Subsequencia Crescente Máxima
def lis(arr):
  n = len(arr)
  dp = [1] * n

  for i in range(n):
    for j in range(i):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)

def main():
  n = int(input())
  arr = list(map(int, input().split()))

  print(lis(arr))

  return 0

if __name__ == "__main__":
  main()