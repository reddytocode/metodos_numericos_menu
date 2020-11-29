expresion_f_x = None


def metodo_trapeziodal_modificado():
    global expresion_f_x
    import scipy
    import numpy as np
    import matplotlib.pyplot as plt
    import numexpr as ne

    expresion_f_x = input("Ingrese f(x), ej: ((1/exp(x))*(x **((c+d)-1)) >> ")
    ##fx = lambda x: 1/(o*np.sqrt(2*np.pi) * np.exp(-(1/2)*(pow((x-u)/o), 2)))
    #fx = lambda x: (x ** 2)
    def fx(x):
        global expresion_f_x
        return ne.evaluate(expresion_f_x)

    #fx = lambda x: np.power((1/np.e),x) * np.power(x,((c+d)-1))

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
metodo_trapeziodal_modificado()

