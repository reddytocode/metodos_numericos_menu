import scipy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def dydx(x, y):
    return np.power(x,2)- (np.power(y,3)/5)

n = 10000
x0 = 1
xf = 3
y0 = 5

x=[x0]
y = [y0]

h = (xf - x0)/n

for i in range(n):
    k0 = dydx(x0,y0)
    k1 = dydx(x0+h,y0+h*k0)
    y0 = y0 + (h/2)*(k0+k1)
    y.append(y0)
    x0 = x0 + h
    x.append(x0)
##print(x)
print(y[-1])
