def main():
  n = int(input())
  m = [[-1] * (n + 2)]

  for i in range(n):
    m.append([-1] + list(map(int, input().split())) + [-1])

  m.append([-1] * (n + 2))

  for r in m:
    print(r)

  return 0

if __name__ == "__main__":
  main()