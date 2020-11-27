##import matplotlib.pyplot as plt  # importando libreria para graficar
expresion_f = None

def metodo_punto_falso():
    global expresion_f

    import numpy as np  # math con superopoderers
    import numexpr as ne

    expresion_f = input("Ingrese f(x), ej: (4*x**2-2*x-1) >> ")
    
    def f(x):
        global expresion_f
        return ne.evaluate(expresion_f)
        #f = lambda x: 4*x**2-2*x-1
        #np.power(np.e,x) - np.tan(x)
        #np.sin(x) + np.log(x)
        #x**3 - 10*x - 5
        #np.sqrt(x**3*np.sin(x))- np.log(np.cos(x))
        #np.power(np.sin(x), 1/3) - (2*np.power(np.cos(x), 1/2)) + (3*x) - 1

    def bolzano(a, b):
        return a * b > 0

    def punto_falso(f, a, b):
        i = 0
        while True:
          x = b - f(b)*(a-b)/(f(a)-f(b))
          if bolzano(f(a), f(x)):
            a = x
          else:
            b = x
          if i==5:
            break
          i = i + 1
        return x
        res = punto_falso(f, 0.2, 1.2)

    
    print(res)

  #metodo_punto_falso()
