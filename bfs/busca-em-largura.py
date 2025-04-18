# Gincana (OBI 2011)

from collections import deque

def main():
  n, m = map(int, input().split())
  students = {}
  grupos = []

  for _ in range(m):
    i, j = map(int, input().split())

    if i not in students:
      students[i] = []
    students[i].append(j)

    if j not in students:
      students[j] = []
    students[j].append(i)
  
  visitados = set()

  for aluno in range(1, n + 1):
    if aluno not in visitados:
      grupo_atual = []
      fila = deque([aluno])
      while fila:
        atual = fila.popleft()
        if atual not in visitados:
          visitados.add(atual)
          grupo_atual.append(atual)
          for amigo in students.get(atual, []):
            fila.append(amigo)

      grupos.append(grupo_atual)

  print(len(grupos))

if __name__ == "__main__":
  main()