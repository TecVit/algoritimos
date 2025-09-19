def main():
  qtd_row, qtd_coluns = map(int, input().split())
  
  dp = [[0] * (qtd_coluns + 1) for _ in range(qtd_row + 1)]

  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  for i in range(1, qtd_row + 1):
    for j in range(1, qtd_coluns + 1):
      if a[i-1] == b[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])

  print(dp[qtd_row][qtd_coluns])

  i, j = qtd_row, qtd_coluns
  lcs = []

  while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
      lcs.append(a[i-1])
      i -= 1
      j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
      i -= 1
    else:
      j -= 1

  lcs.reverse()
  print(*lcs)

  return 0

if __name__ == "__main__":
  main()