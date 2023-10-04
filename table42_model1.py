
# import the math module 
import math 

#initial guess
u = [0,0]
#step size
alpha_init = 0.004
c = 0.4 # 0<c<1
r = 0.5 # 0<r<1

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



m_old = 10**100 #large dummy value
m_new = model1(u[0], u[1])

# Steepest Descent Algorithm
while m_new<m_old:
    
    # Update m_old
    m_old = m_new

    # Compute the gradient of the model1 function with respect to u
    df_dx = 2*a1*(u[0] + 1)*(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2*a2*(u[0] - 1)*(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g1
    df_dy = 2*a1*(u[1] + 1)*(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2*a2*(u[1] + 1)*(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g2

    # Compute the direction vector h
    h = [-df_dx, -df_dy]
    
    ##Backtracking line search
    alpha = alpha_init/r
    
    mx = 10**100 #large dummy value
    while mx > m_new + c*alpha*(h[0] * df_dx + h[1] * df_dy):
        alpha *= r  # Reduce alpha
        ux = [u[0]+alpha*h[0], u[1]+alpha*h[1]]
        mx = model1(ux[0], ux[1])
    m_new = mx
    u=ux
# The minimum value of the model1 function is m* = m_old, and the optimal u* is u - alpha * h
m_star = m_old
u_star = [round(u[0] - alpha * h[0],5), round(u[1] - alpha * h[1],5)]

print("Minimum Value of model1 Function:", round(m_star,9))
print("Optimal u:", u_star)    