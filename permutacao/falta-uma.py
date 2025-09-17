from itertools import permutations
import math

def main():
  n = int(input())
  numbers = set()

  for _ in range(math.factorial(n) - 1):
    row = input()
    numbers.add(tuple(row.split()))

  elements = ''.join(tuple(row.split()))
  todas_perms = set(permutations(elements))
  res = todas_perms - numbers

  for perm in sorted(res):
    print(' '.join(perm))

if __name__ == "__main__":
  main()