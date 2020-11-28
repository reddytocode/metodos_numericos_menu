# Algoritmo de punto fijo
# [a,b] intervalo de búsqueda
# error = tolera

import numpy as np
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

# INGRESO
fx = lambda x: np.exp(-x) - x
gx = lambda x: np.exp(-x)

a = 0       # intervalo
b = 1
tolera = 0.001
iteramax  = 15      # itera máximo
muestras = 51  # gráfico

tramos = 51

# PROCEDIMIENTO
respuesta = puntofijo(gx,a,tolera)

# SALIDA
print(respuesta)
