# OBI 2024 - Fase 3: Brigadeiros
# Solução com DP invertida em Python

MAXN = 301
INF = int(1e9 + 10)
MAXC = 9 * MAXN

n, k, t = map(int, input().split())
qtd = [0] + list(map(int, input().split()))  # 1-based
x = list(map(int, input().split()))
amigo = [False] * (n + 1)
grupo = []

for i in range(1, n + 1):
  if x[i - 1] == 1:
    amigo[i] = True
    grupo.append(i)

dp = [[[INF] * MAXC for _ in range(k + 1)] for __ in range(2)]

for i in range(2):
  for b in range(k + 1):
    dp[i][b][0] = 0

for a in range(1, n + 1):
  i = a % 2
  for b in range(1, k + 1):
    for c in range(MAXC):
      # Pegar o prato a
      if qtd[a] <= c:
        dp[i][b][c] = min(
          dp[i][b][c],
          dp[1 - i][b - 1][c - qtd[a]] + abs(a - grupo[b - 1])
        )
      # Não pegar o prato a
      dp[i][b][c] = min(dp[i][b][c], dp[1 - i][b][c])

for l in range(MAXC - 1, -1, -1):
  if dp[n % 2][k][l] <= t:
    print(l)
    break