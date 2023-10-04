# Define the Rosenbrock function with parameters a=1 and b=100
def rosenbrock(x, y):
    return (x-1)**2 + 10 * (y - x**2)**2

# Set parameters
a = 1
b = 10
alpha = 0.004
u = [-0.75, 0.7]

# Initialize mold with a dummy value
mold = 10**100
mnew = rosenbrock(u[0], u[1])

# Steepest Descent Algorithm
while mnew<mold:
    # Compute the current value of the Rosenbrock function



    # Update mold
    mold = mnew

    # Compute the gradient of the Rosenbrock function with respect to u
    df_dx = 40*u[0]**3 - 40*u[0]*u[1] +2*u[0] -2
    df_dy = 20 * u[1] - 20 * u[0]**2

    # Compute the direction vector h
    h = [-df_dx, -df_dy]

    # Update u using the steepest descent formula
    u[0] = u[0] + alpha * h[0]
    u[1] = u[1] + alpha * h[1]
    mnew = rosenbrock(u[0], u[1])

# The minimum value of the Rosenbrock function is m* = mold, and the optimal u* is u - alpha * h
m_star = mold
u_star = [u[0] - alpha * h[0], u[1] - alpha * h[1]]

print("Minimum Value of Rosenbrock Function:", m_star)
print("Optimal u:", u_star)
