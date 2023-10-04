from sympy import symbols, diff, Symbol

param_alpha = 0.2
param_u = [-0.75, 0.7]

param_a = 1
param_b = 100

param_a_1 = 2
param_a_2 = 2
param_g_1 = 2
param_g_2 = 2

u_1 = Symbol('u1')
u_2 = Symbol('u2')	
    
h = -1

def rosenbrock():
	# global minimum at (param_a, param_a**2) where ros(x,y)=0

	return 100*(u_2-u_1**2)**2+(1-u_1)**2
	

#def objective_func_1(u):
	#obj = param_a_1(sqrt((1+u[0])**2 + (1+u[1])**2)-sqrt(2))**2 + param_a_2(sqrt((1-u[0])**2 + (1+u[1])**2)-sqrt(2))**2 - param_g_1 * u[0] - param_g_2 * u[1]
	#return obj

def m():
	return rosenbrock()

def compute(u, m):
    evalm = m.subs({u_1:u[0]})
    evalm2 = evalm.subs(u_2, u[1])
    print("New U1 is")
    print(u[1])
    print("what is wrong here?")
    print(evalm2)
    print("why is it not subs u_2?")
    return evalm2 #fuck python and symbolic programming

def deriv(u, m):
	u_1 = symbols('u1')
	u_2 = symbols('u2')
	return diff(m, u_1, u_2).subs({u_1:u[0], u_2:u[1]})

print("before first time calling compute")
m_new = compute(param_u, m())
print("after first time calling compute")

m_old = 10.0**100

while m_new < m_old:
    m_old = m_new
    f = deriv(param_u, m()) # over m?
    h = -f
    param_u[0] = param_u[0] + param_alpha * h #remember this is a list, do these operations work?
    param_u[1] = param_u[1] + param_alpha * h 
    m_new = compute(param_u, m())

m_opt = m_old
u_opt = [param_u[0] - param_alpha * h, param_u[1] - param_alpha * h]

print("optimum value is")
print(m_opt)
print("optimum should be 0")
print("parameters are")
print(u_opt)
