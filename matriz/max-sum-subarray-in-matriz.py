# Dada uma matriz N × M de números positivos, encontre
# o maior sub-retângulo contíguo de tamanho 1 × k 
# (uma linha, largura k) cuja soma seja ≤ S.

def max_sum_subarray(m, k, s):
  max_sum = 0

  for row in m:
    n = len(row)
    prefix = [0] * (n + 1)
    for i in range(n):
      prefix[i+1] = prefix[i] + row[i]

    l = 0 # left
    for r in range(n): # right
      while l <= r and (prefix[r + 1] - prefix[l] > s or (r-l-1) > k):
        l += 1
      if l <= r:
        max_sum = max(max_sum, prefix[r+1] - prefix[l])
  
  return max_sum

def main():
  n = int(input())
  k, s = map(int, input().split())

  # k -> Tamanho máximo da janela
  # s -> Soma máxima permitida

  m = []
  for _ in range(n):
    m.append(list(map(int, input().split())))

  print(max_sum_subarray(m, k, s))

  return 0

if __name__ == "__main__":
  main()