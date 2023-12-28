import numpy as np
import sympy as sp

#Scaling sympy functions with lamdify
a = np.arange(10)

t = sp.symbols('t')

func = sp.sinc(2*t)

lfunc = sp.lambdify(t, func, "numpy")

