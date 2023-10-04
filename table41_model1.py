
# import the math module 
import math 

#initial guess
u = [0,0]
#step size
alpha = 0.04
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


#large dummy value
m_old = 10**100
m_new = model1(u[0], u[1])

# Steepest Descent Algorithm
while m_new<m_old:
    # Compute the current value of the model1 function



    # Update m_old
    m_old = m_new

    # Compute the gradient of the model1 function with respect to u
    df_dx = 2*a1*(u[0] + 1)*(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2*a2*(u[0] - 1)*(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g1
    df_dy = 2*a1*(u[1] + 1)*(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2*a2*(u[1] + 1)*(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g2

    # Compute the direction vector h
    h = [-df_dx, -df_dy]

    # Update u using the steepest descent formula
    u[0] = u[0] + alpha * h[0]
    u[1] = u[1] + alpha * h[1]
    m_new = model1(u[0], u[1])

# The minimum value of the model1 function is m* = m_old, and the optimal u* is u - alpha * h
m_star = m_old
u_star = [u[0] - alpha * h[0], u[1] - alpha * h[1]]

print("Minimum Value of model1 Function:", m_star)
print("Optimal u:", u_star)

print("Expecting m∗ = −0.492320397,u∗ = [0.5707 0.3955]")