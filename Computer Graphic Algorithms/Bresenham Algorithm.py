# Bresenham Algorithm
from matplotlib import pyplot as plt

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def Bresenham_integer_line(x1, y1, x2, y2):
  x, y = x1, y1
  Diff_x, Diff_y = abs(x2-x1), abs(y2-y1)
  s1, s2 = sign(x2-x1), sign(y2-y1)
  a, b = [], []

  interchange = 0
  if Diff_y > Diff_x:
    temp = Diff_y
    Diff_y = Diff_x
    Diff_x = temp
    interchange = 1

  e = 2 * Diff_y - Diff_x
  for i in range(0, Diff_x):
    a.append(x)
    b.append(y)

    while e>0 :
      if interchange == 1:
        x = x + s1
      else:
        y = y + s2
      e = e - 2 * Diff_x
    if interchange == 1:
      y = y + s2
    else:
      x = x + s1
    e = e + 2*Diff_y

  a.append(x)
  b.append(y)
  plt.plot(a, b, marker="x", markersize=5)
  plt.title('Bresenham Algorithm')
  plt.show()

Bresenham_integer_line(0,0,10,100)