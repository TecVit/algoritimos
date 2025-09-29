# DFS - Ilhas
def encontrarIlhas(n, m, matriz, origem):
  visitados = set()
  ilhas = []

  for i in range(n):
    for j in range(m):
      if matriz[i][j] == 1 and (i, j) not in visitados:
        ilha = []
        pilha = [(i, j)]

        while pilha:
          x, y = pilha.pop()
          if (x, y) in visitados:
            continue
          visitados.add((x, y))
          ilha.append((x, y))

          for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
              if matriz[nx][ny] == 1 and (nx, ny) not in visitados:
                pilha.append((nx, ny))

        ilhas.append(ilha)

  return ilhas

def main():
  n, m = 3, 4
  matriz = [
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
  ]

  origem = (0, 0)
  print(encontrarIlhas(n, m, matriz, origem))

  return 0

if __name__ == "__main__":
  main()