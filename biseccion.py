import numpy as np  # math con superopoderers

f = lambda x: np.power(np.e,x)+np.power(2,(1/x))+2*np.cos(x)- 6
    #np.power(np.e,x) + x**3 +2*x**2 + 10*x - 20
    #x * np.log(x) - 10
    
    
    #np.sin(x) - 1/np.sin(x) + 1
    #x**2 + 4

def bolzano(a, b):
    return a * b > 0

def bisectriz(f, a, b):
    i = 0
    while True:
        c = (a + b) / 2.0
        if bolzano(f(a), f(c)):
            a = c
        else:
            b = c
            
        if i == 1000:
          break
        i = i + 1
        
        # if(abs(b-a) < 0.001):
        #     break
    return c

res = bisectriz(f, 1, 3)

print(res,3)
