from collections import deque

def mina(N, matriz):
  dist = [[float('inf')] * N for _ in range(N)]
  dist[0][0] = 0
  
  dq = deque()
  dq.append((0, 0))
  
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]

  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        custo = matriz[nx][ny]
        if dist[x][y] + custo < dist[nx][ny]:
          dist[nx][ny] = dist[x][y] + custo
          if custo == 0:
            dq.appendleft((nx, ny))
          else:
            dq.append((nx, ny))

  return dist[N-1][N-1]

def main():
  n = int(input())
  m = []

  for _ in range(n):
    m.append(list(map(int, input().split())))

  print(mina(n, m))

  return 0

if __name__ == "__main__":
  main()