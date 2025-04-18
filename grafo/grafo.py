def ache_o_custo_mais_baixo(custos):
  menor = float("inf")
  nodo_mais_barato = None
  for nodo in custos:
    if custos[nodo] < menor and nodo not in processados:
      menor = custos[nodo]
      nodo_mais_barato = nodo
  return nodo_mais_barato

grafo = {}
grafo["inicio"] = {"a": 6, "b": 2}
grafo["a"] = {"fim": 1}
grafo["b"] = {"a": 3, "fim": 5}
grafo["fim"] = {}

custos = {"a": 6, "b": 2, "fim": float("inf")}
pais = {"a": "inicio", "b": "inicio", "fim": None}
processados = []

nodo = ache_o_custo_mais_baixo(custos)
while nodo is not None:
  custo = custos[nodo]
  vizinhos = grafo[nodo]
  for n in vizinhos:
    novo_custo = custo + vizinhos[n]
    if custos[n] > novo_custo:
        custos[n] = novo_custo
        pais[n] = nodo
  processados.append(nodo)
  nodo = ache_o_custo_mais_baixo(custos)

# Corrigindo aqui:
pais["inicio"] = None

caminho = []
n = "fim"
while n is not None:
  caminho.insert(0, n)
  n = pais[n]

print("Caminho mais curto:", " → ".join(caminho))
print("Custo total:", custos["fim"])