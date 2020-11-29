import tkinter as tk
from euler import metodo_euler
from tabla_de_diferencias_finitas import metodo_tabla_de_diferencias_finitas
from newton_raphson import metodo_newton_raphson
from punto_falso import metodo_punto_falso
from biseccion import metodo_biseccion
from secante import metodo_secante
from punto_fijo import metodo_punto_fijo
from maller import metodo_maller
from polinomio import metodo_polinomio
from lagrange import metodo_lagrange
from diferencias_divididas import metodo_diferencias_divididas
from simpsom import metodo_simpsom
from taylor import metodo_taylor
from euler_modificado import metodo_euler_modificado
from runge_kutta_segundo import metodo_runge_kutta_segundo

metodo_tabla_de_diferencias_finitas_button = None


root = tk.Tk()
# root.geometry("320x512")
# frame = tk.Frame(root)
# frame.pack()
lab = tk.Label(root, text="Cargando ... ", bg="red", height=820, width=512)
boton_already_clicked = False


def call_function(function):
    global boton_already_clicked
    if(boton_already_clicked == False):
        boton_already_clicked = True
        buttons = [metodo_tabla_de_diferencias_finitas_button,
                   metodo_euler_button,
                   metodo_newton_raphson_button,
                   metodo_punto_falso_button,
                   metodo_biseccion_button,
                   metodo_secante_button,
                   metodo_punto_fijo_button,
                   metodo_maller_button,
                   metodo_polinomio_button,
                   metodo_lagrange_button,
                   metodo_diferencias_divididas_button,
                   metodo_simpsom_button,
                   metodo_taylor_button,
                   metodo_euler_modificado_button,
                   metodo_runge_kutta_segundo_button]
        lab.place(relx=1.5,
                  rely=1.5,
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
    metodo_biseccion_button.place(x=10, y=40)
    metodo_punto_falso_button.place(x=10, y=70)
    metodo_secante_button.place(x=10, y=100)
    metodo_euler_button.place(x=10, y=130)
    metodo_newton_raphson_button.place(x=10, y=160)
    metodo_punto_fijo_button.place(x=10, y=190)
    metodo_maller_button.place(x=10, y=220)
    metodo_polinomio_button.place(x=10, y=250)
    metodo_lagrange_button.place(x=10, y=280)
    metodo_diferencias_divididas_button.place(x=10, y=310)
    metodo_simpsom_button.place(x=10, y=340)
    metodo_taylor_button.place(x=10, y=370)
    metodo_euler_modificado_button.place(x=10, y=400)
    metodo_runge_kutta_segundo_button.place(x=10, y=430)

metodo_tabla_de_diferencias_finitas_button = tk.Button(root,
                                                       fg="blue",
                                                       text="Tabla  de_diferencias_finitas",
                                                       command=lambda: call_function(metodo_tabla_de_diferencias_finitas))

metodo_biseccion_button = tk.Button(root,
                                     fg="blue",
                                     text="Biseccion",
                                     command=lambda: call_function(metodo_biseccion))

metodo_punto_fijo_button = tk.Button(root,
                                     fg="blue",
                                     text="Punto Fijo",
                                     command=lambda: call_function(metodo_punto_fijo))

metodo_punto_falso_button = tk.Button(root,
                                     fg="blue",
                                     text="Punto Falso",
                                     command=lambda: call_function(metodo_punto_falso))
metodo_secante_button = tk.Button(root,
                                     fg="blue",
                                     text="Secante",
                                     command=lambda: call_function(metodo_secante))

metodo_euler_button = tk.Button(root,
                                fg="blue",
                                text="Euler",
                                command=lambda: call_function(metodo_euler))

metodo_newton_raphson_button = tk.Button(root,
                                         fg="blue",
                                         text="Newton Raphson",
                                         command=lambda: call_function(metodo_newton_raphson))

metodo_maller_button = tk.Button(root,
                                         fg="blue",
                                         text="Maller",
                                         command=lambda: call_function(metodo_maller))

metodo_polinomio_button = tk.Button(root,
                                         fg="blue",
                                         text="Polinomio",
                                         command=lambda: call_function(metodo_polinomio))

metodo_lagrange_button = tk.Button(root,
                                         fg="blue",
                                         text="Lagrange",
                                         command=lambda: call_function(metodo_lagrange))

metodo_diferencias_divididas_button = tk.Button(root,
                                         fg="blue",
                                         text="Diferencias Divididas",
                                         command=lambda: call_function(metodo_diferencias_divididas))

metodo_simpsom_button = tk.Button(root,
                                         fg="blue",
                                         text="Simpsom",
                                         command=lambda: call_function(metodo_simpsom))

metodo_taylor_button = tk.Button(root,
                                         fg="blue",
                                         text="Taylor",
                                         command=lambda: call_function(metodo_taylor))

metodo_euler_modificado_button = tk.Button(root,
                                         fg="blue",
                                         text="Euler Modificado",
                                         command=lambda: call_function(metodo_euler_modificado))

metodo_runge_kutta_segundo_button = tk.Button(root,
                                         fg="blue",
                                         text="Runge Kutta",
                                         command=lambda: call_function(metodo_runge_kutta_segundo))
place_buttons()
button = tk.Button(root,
                   text="Salir",
                   fg="red",
                   command=quit)
button.place(x=10, y=460)


root.mainloop()
