def metodo_ec_dif_explicito_parabolico():
    # EDP parabólicas d2u/dx2  = K du/dt
    # método explícito,usando diferencias divididas
    # Referencia: Chapra 30.2 p.888 pdf.912
    #       Rodriguez 10.2 p.406
    import numpy as np
    import matplotlib.pyplot as plt

    # INGRESO
    # Valores de frontera
    Ta = float(input("Introduzca ta (ej; 60): "))
    Tb = float(input("Introduzca tb (ej; 40): "))
    T0 = float(input("Introduzca t0 (ej; 25): "))
    # longitud en x
    a = float(input("Introduzca a (ej; 0): "))
    b = float(input("Introduzca b (ej; 1): "))
    # Constante K
    K = float(input("Introduzca k (ej; 4): "))
    # Tamaño de paso
    dx = float(input("Introduzca dx (ej; 0.1): "))
    dt = dx/10
    # iteraciones en tiempo
    n = int(input("Introduzca n (ej; 200): "))

    # PROCEDIMIENTO
    # iteraciones en longitud
    xi = np.arange(a,b+dx,dx)
    m = len(xi)
    ultimox = m-1

    # Resultados en tabla u[x,t]
    u = np.zeros(shape=(m,n), dtype=float)

    # valores iniciales de u[:,j]
    j=0
    ultimot = n-1
    u[0,:]= Ta
    u[1:ultimox,j] = T0
    u[ultimox,:] = Tb

    # factores P,Q,R
    lamb = dt/(K*dx**2)
    P = lamb
    Q = 1 - 2*lamb
    R = lamb

    # Calcula U para cada tiempo + dt
    j = 0
    while not(j>=ultimot): # igual con lazo for
        for i in range(1,ultimox,1):
            u[i,j+1] = P*u[i-1,j] + Q*u[i,j] + R*u[i+1,j]
        j=j+1

    # SALIDA
    print('Tabla de resultados')
    np.set_printoptions(precision=2)
    print(u)
#metodo_ec_dif_explicito_parabolico()