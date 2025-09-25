def primosAteN(n):
  res = []

  if n < 2:
    return res;

  primo = [True] * (n + 1)
  primo[0] = primo[1] = False

  p = 2
  while p * p <= n:
    if primo[p]:
      for mult in range(p * p, n + 1, p):
        primo[mult] = False
    p += 1

  res = [str(i) for i in range(n + 1) if primo[i]]

  return res

def main():
  n = int(input())
  primos = primosAteN(n)
  
  print(*primos)

  return 0

if __name__ == "__main__":
  main()