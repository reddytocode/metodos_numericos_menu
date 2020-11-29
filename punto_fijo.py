expresion_fx = None
expresion_gx = None

def metodo_punto_fijo():
    # Algoritmo de punto fijo
    # [a,b] intervalo de búsqueda
    # error = tolera
    global expresion_fx
    global expresion_gx
    
    import numpy as np
    import numexpr as ne

    # INGRESO
    #fx = lambda x: np.exp(-x) - x
    #gx = lambda x: np.exp(-x)


 

    expresion_fx = input("Ingrese f(x), ej: (exp(x) - x) >> ")
    expresion_gx = input("Ingrese g(x), ej: (exp(-x)) >> ")
    
    a = float(input("a, ej: 0 >> "))
    b = float(input("b, ej: 1 >> "))
    tolera =float(input("tolera, ej: 0.001 >> "))
    #iteramax =float(input("iteramax, ej: 15 >> "))
    
        
    def fx(x):
        global expresion_fx
        return ne.evaluate(expresion_fx)
    def gx(x):
        global expresion_gx
        return ne.evaluate(expresion_gx)



    def puntofijo(gx,a,tolera, iteramax=15 ):
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

    
    #a = 0       # intervalo
    #b = 1
    #tolera = 0.001
    #iteramax  = 15      # itera máximo
    muestras = 51  # gráfico

    tramos = 51
    # PROCEDIMIENTO
    respuesta = puntofijo(gx,a,tolera)

    # SALIDA
    print(respuesta)
    
#metodo_punto_fijo()
