expresion_f_x = None
expresion_df_x = None


def metodo_newton_raphson():
    global expresion_f_x
    global expresion_df_x
    # metodo de  Newton-Rapson

    import numpy as np
    import numexpr as ne

    expresion_f_x = input("Ingrese f(x), ej: (x**3 - 5*x+1) >> ")
    expresion_df_x = input("Ingrese la derivada de f(x), ej: (3*x**2 - 5) >> ")

    def f(x):
        global expresion_f_x
        return ne.evaluate(expresion_f_x)
        # return x**3 - 5*x+1
    #np.log(x)- x + 2
    # x-2*np.cos(x)
    #x*np.power(np.e,x) - 2
    #x**3 - 2*(x**2) + 5*x - 5

    def df(x):
        global expresion_f_x
        return ne.evaluate(expresion_df_x)
        # return 3*x**2 - 5
    # (1/x)-1
    #1 + 2*np.sin(x)
    # np.power(np.e,x)+x*np.power(np.e,x)
    #3*x**2 - 4*x + 5

    x0 = 1
    tolera = 0.001

    tabla = []
    tramo = abs(2*tolera)
    x1 = x0
    while (tramo >= tolera):
        xnuevo = x1 - f(x1)/df(x1)
        tramo = abs(xnuevo-x1)
        tabla.append([x1, xnuevo, tramo])
        x1 = xnuevo

    # convierte a una lista en arreglo.
    tabla = np.array(tabla)
    n = len(tabla)

    # salida
    print(['x1', 'xnuevo', 'tramo'])
    np.set_printoptions(precision=4)
    print(tabla)
    print('raiz en: ', x1)
    print('con error de: ', tramo)


# descomentar para probar este archivo
# metodo_newton_raphson()
