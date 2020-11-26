import numexpr as ne
import scipy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# expresion = input("Ingrese la formula dydx: ")


def dydx(x, y):
    # global expresion
    # x**2 - (y**3)/5
    return np.power(x, 2) - (np.power(y, 3)/5)
    # return ne.evaluate(expresion)


n = 100000
x0 = 1
xf = 3
y0 = 5

x = [x0]
y = [y0]

h = (xf - x0)/n

for i in range(n):
    y0 = y0 + h*dydx(x0, y0)
    y.append(y0)
    x0 = x0 + h
    x.append(x0)

print(y[-1])
