import numpy as np
#from scipy import linalg
import matplotlib.pyplot as plt
#horarios
# x5 = [2,2,2,2,5,2,2,2,3,3,2,3,3,2.2,2,10,2,2,2]
#promedio
x2 = [8.7,7.5,8.1,7.7,6.4,7.5,6.5,7.5,6.5,6.5,7.1,7.0,5.5,6.6,6.8,6.8,6.5,6.2,8.5]
#recreo
x6 = [10,10,5,7,20,20,10,15,10,10,10,10,20,6,17,5,10,20,10]
#edad
x1 = [19,19,20,19,22,19,20,23,19,19,19,29,26,19,20,22,19,22,20]

#peso corporal
x3 = [69,90,61,68,74,85,65,60,60,76,59,74,62,71,48,59,62,59,60]

#estatura
x4 = [1.71,1.79,1.68,1.70,1.60,1.75,1.70,1.58,1.63,1.70,1.56,1.70,1.60,1.71,1.50,1.70,1.69,1.77,1.70]
#unos
x7 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

matrices =[x6]
matriz =[x7,x4,x3,x2,x1]
def trasponer(m):

    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t
traspuesta = trasponer(matriz)
print("--------EJEMPLO DE CLASES------")
print("--------MATRIZ------")
for linea in matriz:
    for elemento in linea:
        print(elemento,end=" ")
    print()
print("------TRASPUESTA--------")

for linea in traspuesta:
    for elemento in linea:
        print(elemento,end=" ")
    print()
print("------MULTIPLICACION--------")
def multiplicacion_matrices(m1,m2):
    if len(m1[0]) == len(m2):

        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    #print((i,j),(i,K),(j,k),(k,j))
                    m3[i][j]+= m1[i][k]*m2[k][j]
        return m3
    else:
        return None
c = multiplicacion_matrices(matriz,traspuesta)
if c== None:
    print("no se puede multiplicar")
else:
    for fila in c:
        print("[",end=" ")
        for elemento in fila:
            print(elemento, end="    ||    ")
        print("]")
 
print("INVERSA DE C:")
matriz_Inv = np.linalg.inv(c)
print(matriz_Inv)

print("MULTIPLICACION traspuesta * x6")

d = multiplicacion_matrices(matrices,traspuesta)
if d == None:
    print("no se puede multiplicar")
else:
    for fila in d:
        print("[",end=" ")
        for elemento in fila:
            print(elemento, end="    ")
        print("]")

print("betas")



P = multiplicacion_matrices(d,matriz_Inv)
if P == None:
    print("no se puede multiplicar")
else:
    for fila in P:
        print("[",end=" ")
        for elemento in fila:
            print(elemento, end="    ")
        print("]")
