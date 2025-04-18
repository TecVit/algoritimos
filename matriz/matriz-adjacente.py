# Quadrado Mágico (OBI 2011)

def main():
  n = int(input())
  m = [[0 for _ in range(n)] for  _ in range(n) ]

  for i in range(n):
    row = [int(x) for x in input().split()]
    m[i] = row

  # Verificando Linhas e Colunas
  sum_row = 0
  sum_column = 0
  for i in range(n): # Complexidade = O(n²)
    sum_c = 0
    for j in range(n):
      sum_c += m[j][i]
    
    if i == 0:
      # Verificando Linhas
      sum_row = sum(m[i])
      # Verificando Linhas
      sum_column = sum_c
    else:
      if sum_row != sum(m[i]):
        print("0")
        return
      if sum_column != sum_c:
        print("0")
        return
      
  # Verificando Diagonais
  sum_d1 = 0
  sum_d2 = 0
  for i in range(n): # Complexidade = O(n²)
    d1 = m[i][i]
    d2 = m[n - i -1][i]
    sum_d1 += d1
    sum_d2 += d2

  if sum_d1 != sum_d2 or sum_d1 != sum_column or sum_d1 != sum_row or sum_d2 != sum_column or sum_d2 != sum_row:
    print("0")
    return
  else:
    print(sum_row)
    return
      
if __name__ == "__main__":
  main()