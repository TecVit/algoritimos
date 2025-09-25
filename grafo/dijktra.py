import heapq

def dijktra(n, grafo, origem):
  INF = float("inf")
  dist = [INF] * (n + 2)
  dist[origem] = 0

  heap = [(0, origem)]

  while heap:
    d, u = heapq.heappop(heap)

    if d > dist[u]:
      continue

    for v, peso in grafo[u]:
      if dist[u] + peso < dist[v]:
        dist[v] = dist[u] + peso
        heapq.heappush(heap, (dist[v], v))

  return dist

def main():
  n, m = map(int, input().split())
  grafo = [[] for _ in range(n + 2)]

  for _ in range(m):
    try:
      u, v, w = map(int, input().split())
      grafo[u].append((v, w))
      grafo[v].append((u, w))
    except:
      pass
    
  origem = 0
  dist = dijktra(n, grafo, origem)
  
  print(dist[n + 1])

  return 0

if __name__ == "__main__":
  main()