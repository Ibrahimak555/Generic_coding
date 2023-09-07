# Bresenham Circle Generation Algorithm
import matplotlib.pyplot as plt

def bresenham_circle(x0, y0, radius):
  x, y = 0, radius
  err = 3 - 2*radius
  points = []

  while x <= y:
    points.append((x0 + x, y0 + y))
    points.append((x0 + y, y0 + x))
    points.append((x0 - y, y0 + x))
    points.append((x0 - x, y0 + y))
    points.append((x0 - x, y0 - y))
    points.append((x0 - y, y0 - x))
    points.append((x0 + y, y0 - x))
    points.append((x0 + x, y0 - y))

    if err<0:
      err = err + 4*x + 6
    else:
      y -= 1
      err = err + 4*(x-y) + 10
    x += 1

  plt.axis('equal')
  plt.scatter([x for x, y in points], [y for x, y in points])
  plt.show()

x = int(input("x:"))
y = int(input("y:"))
r = int(input("radius :"))
bresenham_circle(x, y, r)