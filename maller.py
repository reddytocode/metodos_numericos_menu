expresion_f_x = None

def metodo_maller():
    global expresion_f_x

    import numpy as np  # math con superopoderers
    import numexpr as ne

    expresion_f_x = input("Ingrese f(x), ej: (x**2 + 4) >> ")
    
    def f(x):
        global expresion_f_x
        return ne.evaluate(expresion_f_x)   
    
    
    #f = lambda x: x**2 + 4

    def sign(number: float) -> float:
        return number/abs(number)

    if __name__ == '__main__':
        X = [2, 2.4, 2.9]
        x0, x1, x2 = X

        for iteracion in range(1):
            print("\n---------------\nITERACION ", iteracion+1, "\n---------------")
            h1 = x1 - x0
            h2 = x2 - x1
            print("x0", "x1", "x2")
            print(x0, x1, x2)
            print(f(x0), f(x1), f(x2))
            print("h1", h1)
            print("h2", h2)

            delta1 = (f(x1)- f(x0))/h1
            print("delta1", delta1)

            delta2 = (f(x2) - f(x1)) / h2
            print("delta2", delta2)

            a = (delta2 - delta1)/(h2 + h1)
            print("a", a)

            b = a * h2 + delta2
            print("b", b)

            c = f(x2)
            print("c", c)

            x3 = x2 + ((-1*2*c)/(b + (sign(b) * np.power(((b*b)-(4*a*c)), 0.5))))
            print("x3", np.round(x3,1))

            relative_percent_error = abs((x3 - x2)/x3)*100

            print("relative error", round(relative_percent_error,1), "%")

            x0 = x1
            x1 = x2
            x2 = x3

            print("x0", "x1", "x2")
            print(x0, x1, np.round(x2,1))
#metodo_maller()
