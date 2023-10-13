# import the math module 
import math 
import numpy as np


def func(paramas, paramgs, us):

    m_new = np.dot(paramgs,us)
    print(m_new)
    #1
    for i in range(1,10):
        m_new += paramas[i -1] * (np.sqrt(us[2 *i -1 -1]**2 + (1 + us[2 *i -1])**2) - 1)**2
    #2
    for i in range(1,9):
        m_new += paramas[i +10 -1] * (np.sqrt((1 + us[2 *i +1 -1])**2 + (1 + us[2 *i +2 -1])**2) - np.sqrt(2))**2
    #3
    for i in range(1,9):
        m_new += paramas[i +19 -1] * (np.sqrt((1 - us[2 *i -1 -1 -1])**2 + (1 + us[2 *i -1])**2) - np.sqrt(2))**2     
    #4
    for i in range(1,30):
        m_new += paramas[i +28 -1] * (np.sqrt((1 + us[2 *i +20 -1] - us[2 *i -1])**2 + (us[2 *i +19 -1] - us[2 *i -1 -1])**2) - 1)**2  
    #5
    for i in range(1,36):
        m_new += paramas[i +58 -1] * (np.sqrt((1 + us[2 *i +1 + 2 *math.floor((i -1) /9) -1] - us[2 *i -1 + 2 *math.floor((i -1) /9) -1])**2 + (us[2 *i +2 + 2 *math.floor((i -1) /9) -1] - us[2 *i + 2 *math.floor((i -1) /9) -1])**2) - 1)**2  
    #6
    for i in range(1,27):
        m_new += paramas[i +94 -1] * (np.sqrt((1 + us[2 *i +21 + 2 *math.floor((i -1) /9) -1] - us[2 *i -1 + 2 *math.floor((i -1) /9) -1])**2 + (us[2 *i +22 + 2 *math.floor((i -1) /9) -1] - us[2 *i + 2 *math.floor((i -1) /9) -1])**2) - np.sqrt(2))**2    
    #7
    for i in range(1,27):
        m_new += paramas[i +121 -1] * (np.sqrt((1 + us[2 *i +19 + 2 *math.floor((i -1) /9) -1] + us[2 *i +1 + 2 *math.floor((i -1) /9) -1])**2 + (1 + us[2 *i +20 + 2 *math.floor((i -1) /9) -1] - us[2 *i +2 + 2 *math.floor((i -1) /9) -1])**2) - np.sqrt(2))**2       
    return m_new

# Steepest Descent Algorithm


print(func(np.ones(150), np.ones(150), np.zeros(150)))


def gradients(paramas, paramgs, us):

    #how many different us[ -1] are there? 
    # =============================================================================
    #     2*i-1, 1,3,4
    #     2*i, 1,3,4
    #     2*i+1, 2
    #     2*i+2, 2
    #     2*i+20, 4
    #     2*i+19, 4

    #     2*i+1+2*math.floor((i -1)/9), 5,7
    #     2*i-1+2*math.floor((i -1)/9), 5,6
    #     2*i+2+2*math.floor((i -1)/9), 5,7
    #     2*i+21+2*math.floor((i -1)/9), 6
    #     2*i+22+2*math.floor((i -1)/9), 6
    #     2*i+19+2*math.floor((i -1)/9), 7
    #     2*i+20+2*math.floor((i -1)/9), 7
    # =============================================================================

    f_new = - paramgs
    for i in range(1,10):
        u2i_1 = us[2 *i -1 -1]
        u2i = us[2 *i -1]

        dmdu2i_1 = paramas[i -1] *(us[2 *i -1 -1]**2 + (us[2 *i -1] + 1)**2 - 1)
        dmu2i = paramas[i -1] *(us[2 *i -1 -1]**2 + (us[2 *i -1] + 1)**2 - 1)
    #2
    for i in range(1,9):
        u2i__1 = us[2 *i +1 -1]
        u2i__2 = us[2 *i +2 -1]     

        dmdu2i__1 = paramas[i +10 -1] *(us[2 *i +1 -1]**2 + (us[2 *i +2 -1]+ 1)**2 -np.sqrt(2) + 1)
        dmdu2i__2 = paramas[i +10 -1] *(us[2 *i +1 -1]**2 + (us[2 *i +2 -1]+ 1)**2 -np.sqrt(2) + 1)

    gradients = np.zeros(80)
    for i in us:
        gradients[i] = f_new #meeeeeh
    return gradients

    #18. Okt first mid-term exam


def steepest_decent(func, paramas, paramgs, us, alpha, gradients):
    #large dummy value
    m_old = 10**100
    m_new = func(paramas,paramgs,us)

    while m_new<m_old:
        # Compute the current value of the model1 function
        # Update m_old
        m_old = m_new

        # Compute the gradient of the model1 function with respect to u
        #df_dx = 2*a1*(u[0 -1] + 1)*(math.sqrt((u[0 -1] + 1)**2 + (u[1 -1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0 -1] + 1)**2 + (u[1 -1] + 1)**2) + 2*a2*(u[0 -1] - 1)*(math.sqrt((1 - u[0 -1])**2 + (u[1 -1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0 -1])**2 + (u[1 -1] + 1)**2) - g1
        #df_dy = 2*a1*(u[1 -1] + 1)*(math.sqrt((u[0 -1] + 1)**2 + (u[1 -1] + 1)**2) - math.sqrt(2))/math.sqrt((u[0 -1] + 1)**2 + (u[1 -1] + 1)**2) + 2*a2*(u[1 -1] + 1)*(math.sqrt((1 - u[0 -1])**2 + (u[1 -1] + 1)**2) - math.sqrt(2))/math.sqrt((1 - u[0 -1])**2 + (u[1 -1] + 1)**2) - g2

        # Compute the direction vector h
        h = gradients(paramas, paramgs, us) * (-1)

        # Update u using the steepest descent formula
        h_alpha = h * alpha
        for idx, u in enumerate(us):
            u = u + h_alpha[idx] #will this update us?
        m_new = func(paramas, paramgs, us)     

        # The minimum value of the model1 function is m* = m_old, and the optimal u* is u - alpha * h    
    m_star = m_old
    u_star = us - h_alpha

    print("Minimum Value of model1 Function:", m_star)
    print("Optimal u:", u_star)

    print("β according to Eq. (4.8) requires the least iterations. m∗ = −0.97803880, u∗ =[0.1148 0.1673 0.0489 0.1065 0.0329 0.0685 0.0436 0.0390 0.0639 0.0226 0.0815 0.0161149 0.0904 0.0102 0.0876 −0.0087 0.0851 −0.0522 0.1221 −0.1484 0.2031 0.3337 0.1275 0.2305 0.1032 0.1254 0.1197 0.0553 0.1459 0.0254 0.1750 0.0166 0.2054 0.0099 0.2329 −0.0173 0.2451 −0.1062 0.2612 −0.2662 0.3275 0.5355 0.2346 0.3367 0.2199 0.1473 0.2196 0.0561 0.2336 0.0171 0.2653 0.0020 0.3189 −0.0125 0.3968 −0.0511 0.4832 −0.1454 0.4773 −0.3626 0.5957 0.8310 0.4409 0.3355 0.3709 0.1572 0.3208 0.0591 0.3065 0.0093 0.3326 −0.0211 0.4031 −0.0557 0.5233 −0.1183 0.7062 −0.2429 0.9915 − 0.5251 -1]T")