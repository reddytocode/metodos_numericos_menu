expresion_fx = None

def metodo_punto_fijo():
    # Algoritmo de punto fijo
    # [a,b] intervalo de búsqueda
    # error = tolera
    global expresion_fx
    import numpy as np

    # INGRESO
    #fx = lambda x: np.exp(-x) - x
    gx = lambda x: np.exp(-x)

    a = 0       # intervalo
    b = 1
    tolera = 0.001
    iteramax  = 15      # itera máximo
    muestras = 51  # gráfico

    tramos = 51

    expresion_fx = input("Ingrese f(x), ej: (exp(x) - x) >> ")
    a = float(input("a, ej: 0 >> "))
    #p = float(input("m, ej: 1.2 >> "))
        
    def f(x):
        global expresion_fx
        return ne.evaluate(expresion_fx)



    def puntofijo(gx,a,tolera, iteramax = 15):
        i = 1 # iteración
        b = gx(a)
        tramo = abs(b-a)
        while(tramo>=tolera and i<=iteramax ):
            a = b
            b = gx(a)
            tramo = abs(b-a)
            i = i+1
        respuesta = b
        # Validar respuesta
        if (i>=iteramax ):
            respuesta = np.nan
        return(respuesta)

    # PROGRAMA ---------

    

    # PROCEDIMIENTO
    respuesta = puntofijo(gx,a,tolera)

    # SALIDA
    print(respuesta)
metodo_punto_fijo()
