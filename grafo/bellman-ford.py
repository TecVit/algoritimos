def floyd_warshall(grafo):
  n = len(grafo)
  dist = [row[:] for row in grafo]
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  return dist

def bellman_ford(grafo, inicio):
  n = len(grafo)
  dist = [float('inf')] * n
  dist[inicio] = 0
  
  for _ in range(n - 1):
    for u in range(n):
      for v, peso in grafo[u]:
        if dist[u] + peso < dist[v]:
          dist[v] = dist[u] + peso
  
  for u in range(n):
    for v, peso in grafo[u]:
      if dist[u] + peso < dist[v]:
        print("Ciclo negativo detectado")
        return None
  
  return dist