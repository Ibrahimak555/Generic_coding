# Midpoint Ellipse Generation Algorithm
import matplotlib.pyplot as plt

def plot_points(xc, yc, x, y):
    plt.scatter(xc + x, yc + y, color='blue', s=1)
    plt.scatter(xc - x, yc + y, color='blue', s=1)
    plt.scatter(xc + x, yc - y, color='blue', s=1)
    plt.scatter(xc - x, yc - y, color='blue', s=1)

def draw_ellipse(a, b, xc, yc):
    a_sq = a * a
    b_sq = b * b
    two_a_sq = 2 * a_sq
    two_b_sq = 2 * b_sq
    x = 0
    y = b
    p = round(b_sq - (a_sq * b) + (0.25 * a_sq))

    plot_points(xc, yc, x, y)

    while (two_b_sq * x) < (two_a_sq * y):
        x += 1
        if p < 0:
            p += b_sq * (2 * x + 1)
        else:
            y -= 1
            p += b_sq * (2 * x + 1) - a_sq * (2 * y - 1)
        plot_points(xc, yc, x, y)

    p = round(b_sq * (x + 0.5) * (x + 0.5) + a_sq * (y - 1) * (y - 1) - a_sq * b_sq)

    while y > 0:
        y -= 1
        if p > 0:
            p += a_sq * (1 - 2 * y)
        else:
            x += 1
            p += b_sq * (2 * x + 1) + a_sq * (1 - 2 * y)
        plot_points(xc, yc, x, y)

    plt.plot(xc, yc, color='blue', marker="x", markersize=5)
    plt.axis('equal')
    plt.show()

a = int(input('a:'))
b = int(input('b:'))
center_x = int(input('Midpoint x:'))
center_y = int(input('Midpoint y:'))

draw_ellipse(a, b, center_x, center_y)