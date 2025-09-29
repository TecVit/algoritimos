import math

def area_poligono(vertices):
  n = len(vertices)
  area = 0

  for i in range(n):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i+1)%n]
    area += x1 * y2 - x2 * y1

  return abs(area) / 2

def perimetro_poligono(vertices):
  perimetro = 0
  n = len(vertices)
  for i in range(n):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i+1)%n]
    perimetro += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  return perimetro

def ponto_dentro_poligono(ponto, vertices):
  x, y = ponto
  n = len(vertices)
  dentro = False
  for i in range(n):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i+1)%n]
    if ((y1 > y) != (y2 > y)) and (x < (x2-x1)*(y-y1)/(y2-y1) + x1):
      dentro = not dentro
  return dentro