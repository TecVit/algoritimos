def troco_guloso(valor, moedas):
  res = 0
  for i in range(len(moedas)):
    while valor >= moedas[i]:
      res += 1
      valor -= moedas[i]
  return res

def troco_dp(cache, valor, moedas):
  res = 0

  if cache[valor] != -1:
    return cache[valor]
  
  if valor == 0:
    res = 0
  else:
    res = valor + 1
    for i in range(len(moedas)):
      if valor >= moedas[i]:
        t = troco_dp(cache, valor - moedas[i], moedas) + 1
        if t < res:
          res = t
    cache[valor] = res

  return res

def troco_iterativo(valor, moedas):
  dp = [float("inf")] * (valor + 1)
  dp[0] = 0

  for v in range(valor + 1):
    for m in moedas:
      if v >= m:
        dp[v] = min(dp[v], dp[v - m] + 1)

  return dp[valor] if dp[valor] != float("inf") else -1

def troco(valor, moedas):
  # cache = [-1] * (valor + 1)
  # res = troco_dp(cache, valor, moedas)
  res = troco_iterativo(valor, moedas)
  return res

def main():
  moedas = [1, 5, 10, 21, 25]
  moedas.sort(reverse=True)

  valor = int(input())
  valor_de_troco = troco(valor, moedas)

  print(f"Foi utilizado {valor_de_troco} Moedas")

  return 0

if __name__ == "__main__":
  main()