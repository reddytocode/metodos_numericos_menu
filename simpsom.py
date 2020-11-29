import numpy as np
import matplotlib.pyplot as plt

##fx = lambda x: 1/(o*np.sqrt(2*np.pi) * np.exp(-(1/2)*(pow((x-u)/o), 2)))
fx = lambda x: (x ** 2)
a = float(input("Introduzca a: "))
b = float(input("Introduzca b: "))

intervalo = int(input("Distancias: "))

h = (b - a) / intervalo
xi = a
fx0 = fx(a) #x0
fx1 = fx(fx0 + h) #x1
fx2 = fx(b) #x2
suma = fx0 + fx1 + fx2
for i in range(2, intervalo):
    xi += h
    if i % 2 == 0:
        suma += 4 * fx(xi)
        print("entra")
    else:
        suma += 2 * fx(xi)
        print("none")
print(h)
area = (h/3) * (suma)
print('La Integral es: ', area)
