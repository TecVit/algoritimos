from collections import deque

def dfs(u, parent, adj):
  for v in adj[u]:
    if v != parent:
      dfs(v, u, adj)
            
def bfs(root, adj):
  n = len(adj)
  dist = [-1]*n
  dist[root] = 0
  q = deque([root])

  while q:
    u = q.popleft()
    for v in adj[u]:
      if dist[v] == -1:
        dist[v] = dist[u] + 1
        q.append(v)
        
  return dist