#Test Comment
import numpy as np
import sympy as sp

t, s = sp.symbols('t, s')
a = sp.symbols('a', real=True, positive=True)

#setup the function, transform, and itransform
ft = sp.exp(-a*t)
Fs = sp.laplace_transform(ft,t,s,noconds=True) 
fcheck = sp.inverse_laplace_transform(Fs, s, t, noconds=True)

#evaluates exp(-a*t) at t = 5, a = 5:
eval = fcheck.subs(t,5).subs(a,5)
#turn the symbolic notation to float:
eval.evalf()
#decrease round-pff error:
eval.evalf(chop=True)


