expresion_f_x = None


def metodo_trapezoidal():
    global expresion_f_x 
    # Integración: Regla de los trapecios
    # Usando una función fx()
    import numpy as np
    import matplotlib.pyplot as plt
    import numexpr as ne

    expresion_f_x = input("Ingrese f(x), ej: (x ** 2-(y**3/5)) >> ")
    ##fx = lambda x: 1/(o*np.sqrt(2*np.pi) * np.exp(-(1/2)*(pow((x-u)/o), 2)))
    #fx = lambda x: (x ** 2)
    def fx(x):
        global expresion_f_x
        return ne.evaluate(expresion_f_x)

    # INGRESO
    #fx = lambda x: np.sqrt(x)*np.sin(x)

    # intervalo de integración
    a = float(input("Introduzca a (ej; 1): "))
    b = float(input("Introduzca b (ej; 3): "))
    tramos = int(input("Introduzca tramos (ej; 4): "))

    # PROCEDIMIENTO
    # Regla del Trapecio
    # Usando tramos equidistantes en intervalo
    h = (b-a)/tramos
    xi = a
    suma = fx(xi)
    for i in range(0,tramos-1,1):
        xi = xi + h
        suma = suma + 2*fx(xi)
    suma = suma + fx(b)
    area = h*(suma/2)

    # SALIDA
    print('tramos: ', tramos)
    print('Integral: ', area)
    # GRAFICA
    # Puntos de muestra
    muestras = tramos + 1
    xi = np.linspace(a,b,muestras)
    fi = fx(xi)
    # Linea suave
    muestraslinea = tramos*10 + 1
    xk = np.linspace(a,b,muestraslinea)
    fk = fx(xk)

    # Graficando
    plt.plot(xk,fk, label ='f(x)')
    plt.plot(xi,fi, marker='o',
            color='orange', label ='muestras')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Trapecios')
    plt.legend()

    # Trapecios
    plt.fill_between(xi,0,fi, color='g')
    for i in range(0,muestras,1):
        plt.axvline(xi[i], color='w')

    plt.show()
#metodo_trapezoidal()
