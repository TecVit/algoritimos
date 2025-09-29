import math

def distanciaEuclidiana(p1, p2):
  x1, y1 = p1
  x2, y2 = p2

  dist = math.sqrt((x2 - x1) ** 2 + (y2 -  y1) ** 2)
  return dist

def main():
  x1, y1 = map(int, input().split())
  x2, y2 = map(int, input().split())

  print(distanciaEuclidiana((x1, y1), (x2, y2)))

  return 0

if __name__ == "__main__":
  main()