import scipy
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: np.power((1/np.e),x) * np.power(x,((c+d)-1))

a = float(input("Introduzca a: "))
b = float(input("Introduzca b: "))
c = float(input("Introduzca c: "))
d = float(input("Introduzca d: "))
intervalo = int(input("Distancias: "))

h = (b-a)/intervalo
xi = a
suma = fx(xi)

for i in range(0,intervalo-1,1):
    xi =xi +h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h * (suma/2)

##print('La integra: ',area)

fx = lambda x: np.power((1/np.e),x) * np.power(x,(c-1))
h = (b-a)/intervalo
xi = a
suma = fx(xi)

for i in range(0,intervalo-1,1):
    xi =xi +h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area1 = h * (suma/2)

##print('La integral: ',area1)

fx = lambda x: np.power((1/np.e),x) * np.power(x,(d-1))
h = (b-a)/intervalo
xi = a
suma = fx(xi)

for i in range(0,intervalo-1,1):
    xi =xi +h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area2 = h * (suma/2)

##print('La integra2: ',area2)

fx = lambda x: (area/(area1*area2))*np.power(x,(c-1)) * np.power((1-x),(d-1))
h = (b-a)/intervalo
xi = a
suma = fx(xi)

for i in range(0,intervalo-1,1):
    xi =xi +h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
areaf = h * (suma/2)

print('La integralf: ',areaf)

##muestras = intervalo +1
##xi = np.linspace(a,b,muestras)
##fi = fx(xi)
##
##muestraslinea = intervalo *10 +1
##xk=np.linspace(a,b,muestraslinea)
##fk = fx(xk)

###grafica
##plt.xlabel('x')
##
##plt.ylabel('f(x)')
##plt.title('regla de trapecio')
##plt.legend()
##
##plt.fill_between(xi,0,fi,color='g')
##
##for i in range(0,muestras,1):
##    plt.axvline(xi[i], color='w')
##    
##plt.show()
