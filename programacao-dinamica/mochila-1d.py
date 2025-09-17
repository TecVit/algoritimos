def mochila(pesos, capacidade):
  # pesos = [(kg, valor)]
  dp = [0] * (capacidade + 1)
  
  for kg, valor in pesos:
    for cap in range(capacidade, kg - 1, -1):
      dp[cap] = max(dp[cap], dp[cap - kg] + valor)
  
  return dp[capacidade]

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