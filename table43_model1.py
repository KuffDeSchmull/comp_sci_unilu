
# import the math module 
import math 

#4.6 q4.1   u_0 = 0, r = c = 0.5, nreset = 25,  Model 1: with a = 1, g = 1.

#initial guess
u = [0,0]
#step size
alpha_init = 0.004
c = 0.4 # 0<c<1  ##does not work if c = r? HELP
r = 0.5 # 0<r<1
n_reset = 25

#parameters
a1 = 1
a2 = 1
#forces
g1 = 1
g2 = 1

def model1(x, y):
    length_left_spring = math.sqrt((1 + x)**2 + (1 + y)**2)
    length_right_spring = math.sqrt((1 - x)**2 + (1 + y)**2)
    m = a1 * (length_left_spring - math.sqrt(2))**2 + a2 * (length_right_spring - math.sqrt(2))**2 -g1*x - g2*y
    return m

#compute objective functions
m_old = 10**100 #large dummy value
m_new = model1(u[0], u[1])

#initial dummy derivative values
f_new = [0,0]
h_new = [0,0]

# counter with dummy value
cnt = 0 

#conjugate gradient with backtacking
while m_new < m_old:
    m_old = m_new
    f_old = f_new
    h_old = h_new
    
    # Compute the gradient of the model1 function with respect to u
    df_dx = 2*a1*(u[0] + 1)*(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2*a2*(u[0] - 1)*(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g1
    df_dy = 2*a1*(u[1] + 1)*(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2*a2*(u[1] + 1)*(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g2

    
    f_new = [df_dx, df_dy]
    
    # Determine search direction
    if cnt % n_reset == 0:
        h_new = [-f_new[0], -f_new[1]]
    else:
        # beta according to 4.6 (f_new**T*f_new)/(f_old**T*f_old) ##T means transpose, for matrix multiplication
        beta = (f_new[0]**2+f_new[1]**2)/(f_old[0]**2+f_old[1]**2)
        h_new = [-f_new[0]+max(0,beta)*h_old[0], -f_new[1]]
    #backtracking Line Search
    alpha = alpha_init/r
    mx = 10**100 #large dummy value
    while mx > m_new + c*alpha*(h_new[0]*f_new[0]+h_new[1]*f_new[1]):
        alpha = r*alpha
        ux = [u[0]+alpha*h_new[0],u[1]+alpha*h_new[1]] 
        mx = model1(ux[0],ux[1])
    m_new = mx
    u = ux
    cnt = cnt+1

#completion
# The minimum value of the model1 function is m* = m_old, and the optimal u* is u - alpha * h
m_star = m_old
u_star = [u[0] - alpha * h_new[0], u[1] - alpha * h_new[1]]

print("Minimum Value of model1 Function:", m_star)
print("Optimal u:", u_star)        
    