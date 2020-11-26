import numexpr as ne
import numpy as np

x = 3
y = 2

s = "x**2"

res = ne.evaluate(s)

print(res)
