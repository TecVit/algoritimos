#  W  V  # 1 2 3
# (1, 4) # 4 4 4
# (2, 6) # 4 6 10
# (3, 8) # 4 6 10

# verificar se dp[i][capacidade - peso] + valor > dp[i][j]
# significa que o espaço q estava livre pode ser ocupado 
# por outro item e vai ficar mais valioso do q ja estava

def mochila(pesos, capacidade):
  # pesos = [(kg, valor)]
  qtd_pesos = len(pesos)
  pesos.sort(reverse=True)
  
  dp = [[0] * (capacidade + 1) for _ in range(qtd_pesos + 1)]

  for i in range(1, qtd_pesos + 1):
    kg, valor = pesos[i-1]
    for cap in range(1, capacidade + 1):
      dp[i][cap] = dp[i-1][cap]
      if kg <= cap:
        dp[i][cap] = max(dp[i][cap], dp[i-1][cap - kg] + valor)

  return dp[qtd_pesos][capacidade]

def main():
  p, n = map(int, input().split())
  weights = list()

  for _ in range(n):
    kg, v = map(int, input().split())
    weights.append((kg, v))

  print(mochila(weights, p))

  return 0

if __name__ == "__main__":
  main()