def dfs_iterativo(grafo, inicio):
  visitado = set()
  pilha = [inicio]

  while pilha:
    vertice = pilha.pop()
    if vertice not in visitado:
      visitado.add(vertice)
      print(vertice)

      for vizinho in grafo[vertice]:
        if visitado not in visitado:
          pilha.append(vizinho)

grafo = {
  1: [2, 3],
  2: [1, 4],
  3: [1, 5],
  4: [2],
  5: [3]
}
print(dfs_iterativo(grafo, 1))