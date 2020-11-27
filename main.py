import tkinter as tk
from euler import metodo_euler
from tabla_de_diferencias_finitas import metodo_tabla_de_diferencias_finitas

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
                   metodo_euler_button]
        lab.place(relx=0.5,
                  rely=0.5,
                  anchor='center')
        for butt in buttons:
            butt.place_forget()
        function()
        place_buttons()
        lab.place_forget()
        print("Proceso terminado")
        lab.place_forget()
        boton_already_clicked = False
    else:
        pass


def place_buttons():
    metodo_tabla_de_diferencias_finitas_button.place(x=10, y=10)
    metodo_euler_button.place(x=10, y=40)


metodo_tabla_de_diferencias_finitas_button = tk.Button(root,
                                                       text="Tabla  de_diferencias_finitas",
                                                       command=lambda: call_function(metodo_tabla_de_diferencias_finitas))


metodo_euler_button = tk.Button(root,
                                fg="blue",
                                text="Euler",
                                command=lambda: call_function(metodo_euler))

place_buttons()
button = tk.Button(root,
                   text="Salir",
                   fg="red",
                   command=quit)
button.place(x=10, y=70)


root.mainloop()
