def metodo_tabla_de_diferencias_finitas():
    # Tabla de Diferencias finitas
    # resultado en: [título,tabla]
    # Tarea: verificar tamaño de vectores
    import numpy as np

    # INGRESO, Datos de prueba
    xi_aux = []
    fi_aux = []
    n_1 = 0
    while(True):
        try:
            n_1 = int(input("Cantidad de n >> "))
            break
        except Exception as e:
            pass

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
