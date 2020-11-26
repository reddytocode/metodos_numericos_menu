# def punto_fals():
#     print("punto falso")


# def secante():
#     print("secante")


# opciones = [
#     (0, "Punto Falso", punto_fals),
#     (1, "Secante", secante)]

# print("Ingrese una opción")
# for opcion in opciones:
#     print("{}: {}, ingrese si para correr".format(opcion[0], opcion[1]))
#     correr = input()
#     if(correr == "si"):
#         opcion[2]()


import tkinter as tk
from tablas import tabla_de_diferencias_finitas
from tablas import Euler

def diferencias_finitas():
    print("Correr tabla_de_diferencias_finitas")
    tabla_de_diferencias_finitas()

def euler():
    print("Euler")
    Euler()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="tabla_de_diferencias_finitas",
                   command=diferencias_finitas)
                   
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Euler",
                   command=euler)
slogan.pack(side=tk.LEFT)

root.mainloop()
