def metodo_polinomial():
    import numpy as np
    import matplotlib.pyplot as plt
    # INGRESO, Datos de prueba
    x_aux = []
    y_aux = []
    n_1 = 0
    while(True):
        try:
            n_1 = int(input("Cantidad de n >> "))
            break
        except Exception as e:
            pass
    for _ in range(n_1):
        aux = float(input("x_{} >> ".format(_)))
        x_aux.append(aux)

    for _ in range(n_1):
        aux = float(input("y_{} >> ".format(_)))
        y_aux.append(aux)

    x = np.array(x_aux)
    y = np.array(y_aux)
    
    # Peso corporal[kg]
    #x=np.array([58,62,59,70,85])
    # Recreo
    #y=np.array([10,15,17,25,34])
    #x=np.array([5,12,9])
    #y=np.array([1,7,10])
    #x=np.array([2,4,4,5,9,10,11])
    #y=np.array([4,1,3,1,3,7,5])
    #x=np.array([4,10,11,2,5,4,9])
    #y=np.array([1,7,5,4,1,2,3])

    N=len(x)
    A=np.zeros((N,N))

    for i in range(N):
        A.T[i]=x**i
    a=np.linalg.solve(A,y)

    print(a[-1])
    xteo = np.linspace(min(x),max(x),100)
    yteo=0
    for i in range(N):
        yteo=yteo+a[i]*xteo**i

    #yteo = a[0]+a[1]*xteo+[2]*xteo**2
    plt.plot(x,y,'ro')
    plt.plot(xteo,yteo,'b-')
    plt.show()
metodo_polinomial()
   
