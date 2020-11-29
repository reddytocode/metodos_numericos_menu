import numpy as np
import matplotlib.pyplot as plt
# Peso corporal[kg]
x=np.array([58,62,59,70,85])
# Recreo
y=np.array([10,15,17,25,34])
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

##import numpy as np
##import matplotlib.pyplot as plt
##import math
###anexa a
###w eliminar
##
##archivo =open("Prueba.txt","w")
##
###archivo = int(input("tabla"))
##archivo.write("hola mundo\n ")
##archivo.write("Saludos desde bolivia \n")
##nombre=input("intoduce  tu nombre")
##archivo.write(nombre+'\n')
##numero=int(input("intoduce  tu numero"))
##archivo.write('numero= % s'%numero+'\n')
##n = int (input("¿cuantos deportes? "))
##deportes=[]
##for i in range(n):
##    deporte = input("deporte: ")
##    deportes.append(deporte)
##archivo.write('deportes=%s'%deportes)
##
##archivo.close()
##
##
