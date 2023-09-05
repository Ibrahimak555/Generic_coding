# DDA (Digital Differential Analyzer)
# Generates a line segment between 2 endpoints
# Utilizes the Slope of the line
from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):

    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    steps = max(dx, dy)

    x, y = float(x0), float(y0)
    a, b = [], []

    for i in range(steps):
        a.append(x)
        b.append(y)
        x = x + dx/steps
        y = y + dy/steps

    plt.plot(a, b, marker="x", markersize=5)
    plt.xlim([0,100])
    plt.ylim([0,100])
    plt.title('DDA Algorithm')
    plt.show()

DDA(0, 0, 100, 50)