import sympy
from sympy import symbols#, Symbol
from sympy import diff, exp
import numpy as np


x,y,v,w=symbols("x,y,v,w")
g_1,g_2=symbols("g_1,g_2")
a_1,a_2=symbols("a_1,a_2")

obj_func = a_1 * (sympy.sqrt((1 + x)**2 + (1 + y)**2) - sympy.sqrt(2))**2 + a_2 * (sympy.sqrt((1 - x)**2 + (1 + y)**2) - sympy.sqrt(2))**2 - g_1 *x -g_2 *y

dmdx = diff(obj_func,x)
dmdy = diff(obj_func,y)


dmdx1 = diff((sympy.sqrt((x)**2 + (1 +y)**2) -1)**2, x)
dmdy1 = diff((sympy.sqrt((x)**2 + (1 +y)**2) -1)**2, y)
#print(dmdx1)
#print(dmdy1)


func2 = (sympy.sqrt((1 +x)**2 +(1 +y)**2) - sympy.sqrt(2))**2

dmdx2 = diff(func2,x)
dmdy2 = diff(func2,y)
#print(dmdx2)
#print(dmdy2)

func3 = (sympy.sqrt((1 - x)**2 + (1 + y)**2) - sympy.sqrt(2))**2

dmdx3 = diff(func3,x)
dmdy3 = diff(func3,y)
#print(dmdx3)
#print(dmdy3)

func4 = (sympy.sqrt((1 + x - y)**2 + (v - w)**2) - 1)**2  

dmdx4 = diff((sympy.sqrt((1 + x - y)**2 + (v - w)**2) - 1)**2,x)
dmdy4 = diff((sympy.sqrt((1 + x - y)**2 + (v - w)**2) - 1)**2,y)
dmdv4 = diff((sympy.sqrt((1 + x - y)**2 + (v - w)**2) - 1)**2,v)
dmdw4 = diff((sympy.sqrt((1 + x - y)**2 + (v - w)**2) - 1)**2,w)

#print(dmdx4)
#print(dmdy4)
#print(dmdv4)
#print(dmdw4)

func5 = (sympy.sqrt((1 + x - y)**2 + (v - w)**2) - 1)**2  
dmdx5 = diff(func5,x)
dmdy5 = diff(func5,y)
dmdv5 = diff(func5,v)
dmdw5 = diff(func5,w)

#print(dmdx5)
#print(dmdy5)
#print(dmdv5)
#print(dmdw5)

func6 = (sympy.sqrt((1 + x - y)**2 + (1+ v - w)**2) - sympy.sqrt(2))**2   
dmdx6 = diff(func6,x)
dmdy6 = diff(func6,y)
dmdv6 = diff(func6,v)
dmdw6 = diff(func6,w)

#print(dmdx6)
#print(dmdy6)
#print(dmdv6)
#print(dmdw6)

func7 = (sympy.sqrt((1 - x + y)**2 + (1 + v - w)**2) - sympy.sqrt(2))**2
dmdx7 = diff(func7,x)
dmdy7 = diff(func7,y)
dmdv7 = diff(func7,v)
dmdw7 = diff(func7,w)


xy = [x,y,v,w]
ff = func7

for i in xy:
    for j in xy:
        print(i)
        print(j)
        print(diff(diff(ff,j),i))
