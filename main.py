import tkinter as tk
from euler import metodo_euler
from tabla_de_diferencias_finitas import metodo_tabla_de_diferencias_finitas
from newton_raphson import metodo_newton_raphson
from punto_falso import metodo_punto_falso

metodo_tabla_de_diferencias_finitas_button = None


root = tk.Tk()
# root.geometry("320x512")
# frame = tk.Frame(root)
# frame.pack()
lab = tk.Label(root, text="Cargando ... ", bg="red", height=320, width=512)
boton_already_clicked = False


def call_function(function):
    global boton_already_clicked
    if(boton_already_clicked == False):
        boton_already_clicked = True
        buttons = [metodo_tabla_de_diferencias_finitas_button,
                   metodo_euler_button,
                   metodo_newton_raphson_button,
                   metodo_punto_falso_button]
        lab.place(relx=0.5,
                  rely=0.5,
                  anchor='center')
        for butt in buttons:
            butt.place_forget()
        try:
            function()
        except Exception as e:
            print("Hubo un error, reintente porfavor")
        place_buttons()
        lab.place_forget()
        print("\nProceso terminado\n")
        lab.place_forget()
        boton_already_clicked = False
    else:
        pass


def place_buttons():
    metodo_tabla_de_diferencias_finitas_button.place(x=10, y=10)
    metodo_punto_falso_button.place(x=10, y=40)
    metodo_euler_button.place(x=10, y=70)
    metodo_newton_raphson_button.place(x=10, y=100)

metodo_tabla_de_diferencias_finitas_button = tk.Button(root,
                                                       fg="blue",
                                                       text="Tabla  de_diferencias_finitas",
                                                       command=lambda: call_function(metodo_tabla_de_diferencias_finitas))

metodo_punto_falso_button = tk.Button(root,
                                     fg="blue",
                                     text="Punto Falso",
                                     command=lambda: call_function(metodo_punto_falso))

metodo_euler_button = tk.Button(root,
                                fg="blue",
                                text="Euler",
                                command=lambda: call_function(metodo_euler))

metodo_newton_raphson_button = tk.Button(root,
                                         fg="blue",
                                         text="Newton Raphson",
                                         command=lambda: call_function(metodo_newton_raphson))

place_buttons()
button = tk.Button(root,
                   text="Salir",
                   fg="red",
                   command=quit)
button.place(x=10, y=130)


root.mainloop()
