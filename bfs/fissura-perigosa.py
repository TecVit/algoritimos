from collections import deque

def bfs(m, f, n):
  fila = deque()
  if m[1][1] <= f:
    fila.append((1, 1))

  direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  
  while fila:
    x, y = fila.popleft()
    m[x][y] = '*'

    for dx, dy in direcoes:
      nx, ny = x + dx, y + dy
      if m[nx][ny] != '*' and m[nx][ny] <= f:
        fila.append((nx, ny))

def main():
  n, f = map(int, input().split())
  m = [[10] * (n + 2)]

  for _ in range(n):
    m.append([10] + list(map(int, input())) + [10])

  m.append([10] * (n + 2))

  bfs(m, f, n)

  for i in range(1, n + 1):
    for j in range(1, n + 1):
      print(m[i][j], end="")
    print()

  return 0

if __name__ == "__main__":
  main()