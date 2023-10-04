
param_alpha = 0.02
param_u = [-0.75, 0.7]

param_a = 1 #standard parameters for rosenbrock
param_b = 100 #standard parameters for rosenbrock

rosenbrock = param_b*(param_u[1]-param_u[0]**2)**2+(param_a-param_u[0])**2
dmdu_0 = -2*param_a-4*param_b**2*param_u[0]*(param_u[1]-param_u[0]**2)+2*param_u[0]
dmdu_1 =  2*param_b**2*(param_u[1]-param_u[0]**2)

m_new = rosenbrock
m_old = 10**100
m_opt = 1337
u_opt = param_u

while m_new < m_old:
    m_old = m_new
    f = [2*param_a-4*param_b**2*param_u[0]*(param_u[1]-param_u[0]**2)+2*param_u[0], 2*param_b**2*(param_u[1]-param_u[0]**2)]
    h = [-f[0], -f[1]]
    param_u[0] = param_u[0] + param_alpha*h[0]
    param_u[1] = param_u[1] + param_alpha*h[1]

    m_new = param_b*(param_u[1]-param_u[0]**2)**2+(param_a-param_u[0])**2
    m_opt = m_old
    u_opt = [param_u[0]-param_alpha*h[0], param_u[1]-param_alpha*h[1]] 
    print("Opt m is")
    print(m_opt)
    print("Opt u is")
    print(u_opt)

print("Opt m is")
print(m_opt)
print("Opt u is")
print(u_opt)
