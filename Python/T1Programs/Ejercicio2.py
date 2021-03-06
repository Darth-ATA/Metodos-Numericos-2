#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from Tema1 import *
from sympy import *
from collections import *
import numpy as np

#2. Encuentra una aproximación de la raíz cúbica de 52 con un error menor que 10^(-8)
#   mediante el algoritmo de bisección.

def f(x):
    return x**3-52

x=Bisection(f,float(3),float(4),10**(-8))

print "La raiz cubica de 52 es ", x.x

import matplotlib.pyplot as plt
t1 = np.arange(3.0,4.0,0.1)

plt.grid(true)
plt.plot(t1,f(t1),'k')
plt.ylabel('some numbers')
plt.show()
