# metodo de  Newton-Rapson

import numpy as np
f = lambda x: x**3 -5*x+1
    #np.log(x)- x + 2
    #x-2*np.cos(x)
    #x*np.power(np.e,x) - 2
    #x**3 - 2*(x**2) + 5*x - 5
df = lambda x: 3*x**2 -5
    #(1/x)-1
    #1 + 2*np.sin(x)
    #np.power(np.e,x)+x*np.power(np.e,x)
    #3*x**2 - 4*x + 5

x0 = 1
tolera = 0.001

tabla=[]
tramo = abs(2*tolera)
x1 = x0
while (tramo>= tolera):
    xnuevo = x1 -f(x1)/df(x1)
    tramo = abs(xnuevo-x1)
    tabla.append([x1,xnuevo,tramo])
    x1 =xnuevo
    
#convierte a una lista en arreglo.
tabla = np.array(tabla)
n = len(tabla)

#salida
print(['x1','xnuevo','tramo'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', x1)
print('con error de: ',tramo)
      
