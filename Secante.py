expresion_f_x = None

def metodo_secante():
  global expresion_f_x 
  import numpy as np  # math con superopoderers
  import numexpr as ne

  expresion_f_x = input("Ingrese f(x), ej: (sin(x) - (1/sin(x)) + 1) >> ")
  m = float(input("m, ej: 0.2 >> "))
  p = float(input("m, ej: 1.2 >> "))
    
  def f(x):
      global expresion_f_x
      return ne.evaluate(expresion_f_x)
    #f = lambda x: sin(x) - (1/sin(x)) + 1
    #np.power(np.e,x) + x**3 +2*x**2 + 10*x - 20
    #x * np.log(x) - 10 
    #np.power(np.e,x)+np.power(2,(1/x))+2*np.cos(x)- 6
    #x**3 + 2*x**2 +10*x - 20
    #np.power(np.sin(x), 1/3) - (2*np.power(np.cos(x), 1/2)) + (3*x) - 1
  def secante(f, a, b):
    i = 0
    while True:
      x = b - (b-a)*f(b)/(f(b)-f(a))
      print(x)
      # no funciona para numeros grandes
      # hay que poner que la tarea termine cuando x es el mismo dos veces seguidas, o que la diferencia entre dos resultados es super chiquita
      # puedes cambiar la siguiente linea por 20 o un numero mas grande y ver que imprime
      # por que imprime -> nan
      # lo que significa que hubo alguna operacion con un resultado indeterminado como 0/0 o n/0
      if i==5:
        return x
        break
      i = i + 1
      a = b
      b = x


  res = secante(f, m, p)
  print("respuesta", res)
#metodo_secante()
