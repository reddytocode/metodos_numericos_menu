expresion_f_x = None


def metodo_runge_kutta_segundo():
    global expresion_f_x
    import scipy
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import style
    style.use('ggplot')
    import numexpr as ne

    expresion_f_x = input("Ingrese f(x), ej: (x ** 2-(y**3/5)) >> ")
    ##fx = lambda x: 1/(o*np.sqrt(2*np.pi) * np.exp(-(1/2)*(pow((x-u)/o), 2)))
    #fx = lambda x: (x ** 2)
    def dydx(x,y):
        global expresion_f_x
        return ne.evaluate(expresion_f_x)

    #def dydx(x, y):
        #return np.power(x,2)- (np.power(y,3)/5)

    n = int(input("Introduzca n (ej; 10000): "))
    x0 = float(input("Introduzca x0 (ej; 1): "))
    xf = float(input("Introduzca xf (ej; 3): "))
    y0 = float(input("Introduzca n (ej; 5): "))

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
#metodo_runge_kutta_segundo()
