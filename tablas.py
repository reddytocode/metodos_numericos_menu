def Euler():
    import scipy
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import style
    import numexpr as ne
    style.use('ggplot')
    ##% matplotlib  inline
    ##% config InlineBackend.figure_format = 'svg'
    ###########################################
    ###################################
    ##fx = lambda x: np.power((1/np.e),x) * np.power(x,((c+d)-1))


    expresion = input("Ingrese la formula dydx: ")
    def dydx(x, y):
        global expresion
        # x**2-(y**3)/5
    ##    return np.power(x,2)- (np.power(y,3)/5)
        return ne.evaluate(expresion)

    n = 100000
    x0 = 1
    xf = 3
    y0 = 5

    x=[x0]
    y = [y0]

    h = (xf - x0)/n

    for i in range(n):
        y0 = y0 + h*dydx(x0,y0)
        y.append(y0)
        x0 = x0 + h
        x.append(x0)
    ##print(x)
    print(y[-1])

def tabla_de_diferencias_finitas():
    # Tabla de Diferencias finitas
    # resultado en: [título,tabla]
    # Tarea: verificar tamaño de vectores
    import numpy as np

    # INGRESO, Datos de prueba
    xi_aux = []
    fi_aux = []
    n_1 = int(input("Cantidad de n >> "))
    for _ in range(n_1):
        aux = float(input("x_{} >> ".format(_)))
        xi_aux.append(aux)

    for _ in range(n_1):
        aux = float(input("f_{} >> ".format(_)))
        fi_aux.append(aux)

    # xi = np.array([50, 60, 70, 80, 90, 100])
    # fi = np.array([24.94, 30.11, 36.05, 42.84, 50.57, 59.30])
    xi = np.array(xi_aux)
    fi = np.array(fi_aux)

    # PROCEDIMIENTO

    # Tabla de Diferencias Finitas
    titulo = ['i', 'xi', 'fi']
    n = len(xi)
    ki = np.arange(0, n, 1)
    tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
    tabla = np.transpose(tabla)
    # diferencias finitas vacia
    dfinita = np.zeros(shape=(n, n), dtype=float)
    tabla = np.concatenate((tabla, dfinita), axis=1)
    # Calcula tabla, inicia en columna 3
    [n, m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    while (j < m):
        # Añade título para cada columna
        titulo.append('df'+str(j-2))
        # cada fila de columna
        i = 0
        while (i < diagonal):
            tabla[i, j] = tabla[i+1, j-1]-tabla[i, j-1]
            i = i+1
        diagonal = diagonal - 1
        j = j+1

    # SALIDA
    np.set_printoptions(precision=3)
    print('Tabla Diferencia Finita: ')
    print([titulo])
    print(tabla)

