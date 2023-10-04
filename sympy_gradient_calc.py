import sympy
from sympy import symbols#, Symbol
from sympy import diff, exp


x,y=symbols("x,y")
g_1,g_2=symbols("g_1,g_2")
a_1,a_2=symbols("a_1,a_2")

obj_func = a_1 * (sympy.sqrt((1 + x)**2 + (1 + y)**2) - sympy.sqrt(2))**2 + a_2 * (sympy.sqrt((1 - x)**2 + (1 + y)**2) - sympy.sqrt(2))**2 - g_1*x -g_2*y

dmdx = diff(obj_func,x)
dmdy = diff(obj_func,y)

print("dm/dx is:")
print(dmdx)
print("dm/dy is:")
print(dmdy)