# import the math module 
import math 
import numpy as np

#Model 4a


def model1(paramgs, us):
    x = us[0]
    y = us[1]
    #parameters
    a1 = 1
    a2 = 1
    #forces
    g1 = 1
    g2 = 1
    length_left_spring = math.sqrt((1 + x)**2 + (1 + y)**2)
    length_right_spring = math.sqrt((1 - x)**2 + (1 + y)**2)
    m = a1 * (length_left_spring - math.sqrt(2))**2 + a2 * (length_right_spring - math.sqrt(2))**2 -g1 *x - g2 *y
    return m


def m1dm(paramgs, u):
    #parameters
    a1 = 1
    a2 = 1
    #forces
    g1 = 1
    g2 = 1
    gradient = np.zeros(2)
    gradient[0] = 2 *a1 *(u[0] + 1) *(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2)) /math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2 *a2 *(u[0] - 1) *(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2)) /math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g1
    gradient[1] = 2 *a1 *(u[1] + 1) *(math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) - math.sqrt(2)) /math.sqrt((u[0] + 1)**2 + (u[1] + 1)**2) + 2 *a2 *(u[1] + 1) *(math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - math.sqrt(2)) /math.sqrt((1 - u[0])**2 + (u[1] + 1)**2) - g2
    return gradient


def model4a(paramgs, us):

    m_new = - np.dot(paramgs,us) #verified
    #print(m_new)
    #1
    for i in range(1,11):
        #print(i)
        m_new += (np.sqrt(us[2 *i -1 -1]**2 + (1 + us[2 *i -1])**2) - 1)**2 #verified
    #2
    for i in range(1,10):
        m_new += (np.sqrt((1 + us[2 *i +1 -1])**2 + (1 + us[2 *i +2 -1])**2) - np.sqrt(2))**2 #verified
    #3
    for i in range(1,10):
        m_new += (np.sqrt((1 - us[2 *i -1 -1])**2 + (1 + us[2 *i -1])**2) - np.sqrt(2))**2    #verified
    #4
    for i in range(1,31):
        m_new += (np.sqrt((1 + us[2 *i +20 -1] - us[2 *i -1])**2 + (us[2 *i +19 -1] - us[2 *i -1 -1])**2) - 1)**2  #verified
    #5
    for i in range(1,37):
        m_new += (np.sqrt((1 + us[2 *i +1 + 2 *math.floor((i -1) /9) -1] - us[2 *i -1 + 2 *math.floor((i -1) /9) -1])**2 + (us[2 *i +2 + 2 *math.floor((i -1) /9) -1] - us[2 *i + 2 *math.floor((i -1) /9) -1])**2) - 1)**2  #verified
    #6
    for i in range(1,28):
        m_new += (np.sqrt((1 + us[2 *i +21 + 2 *math.floor((i -1) /9) -1] - us[2 *i -1 + 2 *math.floor((i -1) /9) -1])**2 + (1+ us[2 *i +22 + 2 *math.floor((i -1) /9) -1] - us[2 *i + 2 *math.floor((i -1) /9) -1])**2) - np.sqrt(2))**2    #verified
    #7
    for i in range(1,28):
        m_new += (np.sqrt((1 - us[2 *i +19 + 2 *math.floor((i -1) /9) -1] + us[2 *i +1 + 2 *math.floor((i -1) /9) -1])**2 + (1 + us[2 *i +20 + 2 *math.floor((i -1) /9) -1] - us[2 *i +2 + 2 *math.floor((i -1) /9) -1])**2) - np.sqrt(2))**2     #verified 
    return m_new


#
#print(func(np.ones(80), np.ones(80))) #-43

#first derivative of Model 4a


def gradient4a(paramgs, us):

    f_new = - paramgs # array of 80 derivatives
    #1
    for i in range(1, 11): #verified
        x = us[2 *i -1 -1]
        y = us[2 *i -1]
        #print(2 *i -1 -1)
        #print(2 *i -1)
        dmdux = 2 *x *(np.sqrt(x**2 + (y + 1)**2) - 1) /np.sqrt(x**2 + (y + 1)**2)
        dmduy = 2 *(y + 1) *(np.sqrt(x**2 + (y + 1)**2) - 1) /np.sqrt(x**2 + (y + 1)**2)

        f_new[2 *i -1 -1] += dmdux
        f_new[2 *i -1] += dmduy
    #2
    for i in range(1,10): #verified
        x = us[2 *i +1 -1]
        y = us[2 *i +2 -1]

        dmdux = 2 *(x + 1) *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((x + 1)**2 + (y + 1)**2)
        dmduy = 2 *(y + 1) *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((x + 1)**2 + (y + 1)**2)

        f_new[2 *i +1 -1] += dmdux
        f_new[2 *i +2 -1] += dmduy
        #3
    for i in range(1,10): #verified
        x = us[2 *i -1 -1]
        y = us[2 *i -1]

        dmdux = 2 *(x - 1) *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((1 - x)**2 + (y + 1)**2)
        dmduy = 2 *(y + 1) *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((1 - x)**2 + (y + 1)**2)

        f_new[2 *i -1 -1] += dmdux
        f_new[2 *i -1] += dmduy 
        #4
    for i in range(1,31): #verified
        x = us[2 *i +20 -1]
        y = us[2 *i -1]
        v = us[2 *i +19 -1]
        w = us[2 *i -1 -1]

        dmdux = 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduy = 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduv = 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduw = 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)

        f_new[2 *i +20 -1] += dmdux
        f_new[2 *i -1] += dmduy
        f_new[2 *i +19 -1] += dmduv
        f_new[2 *i -1 -1] += dmduw
        #5
    for i in range(1,37): #verified
        x = us[2 *i +1 + 2 *math.floor((i -1) /9) -1]
        y = us[2 *i -1 + 2 *math.floor((i -1) /9) -1]
        v = us[2 *i +2 + 2 *math.floor((i -1) /9) -1]
        w = us[2 *i + 2 *math.floor((i -1) /9) -1]    

        dmdux = 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduy = 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduv = 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduw = 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)

        f_new[2 *i +1 + 2 *math.floor((i -1) /9) -1] += dmdux
        f_new[2 *i -1 + 2 *math.floor((i -1) /9) -1] += dmduy
        f_new[2 *i +2 + 2 *math.floor((i -1) /9) -1] += dmduv
        f_new[2 *i + 2 *math.floor((i -1) /9) -1] += dmduw        
        #6
    for i in range(1,28): #verified
        x = us[2 *i +21 + 2 *math.floor((i -1) /9) -1]
        y = us[2 *i -1 + 2 *math.floor((i -1) /9) -1]
        v = us[2 *i +22 + 2 *math.floor((i -1) /9) -1]
        w = us[2 *i + 2 *math.floor((i -1) /9) -1]

        dmdux = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(x - y + 1) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2)
        dmduy = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-x + y - 1) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2)
        dmduv = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(v - w + 1) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2)
        dmduw = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2)

        f_new[2 *i +21 + 2 *math.floor((i -1) /9) -1] += dmdux
        f_new[2 *i -1 + 2 *math.floor((i -1) /9) -1] += dmduy
        f_new[2 *i +22 + 2 *math.floor((i -1) /9) -1] += dmduv
        f_new[2 *i + 2 *math.floor((i -1) /9) -1] += dmduw        
        #7
    for i in range(1,28): #verified
        #print(i)
        x = us[2 *i +19 + 2 *math.floor((i -1) /9) -1]
        y = us[2 *i +1 + 2 *math.floor((i -1) /9) -1]
        v = us[2 *i +20 + 2 *math.floor((i -1) /9) -1]
        w = us[2 *i +2 + 2 *math.floor((i -1) /9) -1]

        dmdux = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(x - y - 1) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2)
        dmduy = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-x + y + 1) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2)
        dmduv = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(v - w + 1) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2)
        dmduw = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2)
        #print(dmduw)
        f_new[2 *i +19 + 2 *math.floor((i -1) /9) -1] += dmdux
        f_new[2 *i +1 + 2 *math.floor((i -1) /9) -1] += dmduy
        f_new[2 *i +20 + 2 *math.floor((i -1) /9) -1] += dmduv
        f_new[2 *i +2 + 2 *math.floor((i -1) /9) -1] += dmduw        
    #print(np.arange(1,81))
    return f_new


#print(dmxs1(np.ones(80), np.ones(80))) #-43
#print(dmxs1(np.ones(80), np.zeros(80)))


def hessian4a(paramgs, us):
    f_new = np.empty([80,80])
    for i in range(80):
        f_new[i] = np.zeros(80)
    #print(f_new)
    #1
    for i in range(1, 11): #verified
        xi = 2 *i -1 -1
        yi = 2 *i -1

        x = us[xi]
        y = us[yi]

        dmduxx = 2 *x**2 /(x**2 + (y + 1)**2) - 2 *x**2 *(np.sqrt(x**2 + (y + 1)**2) - 1) /(x**2 + (y + 1)**2)**(3 /2) + 2 *(np.sqrt(x**2 + (y + 1)**2) - 1) /np.sqrt(x**2 + (y + 1)**2)
        dmduxy = 2 *x *(y + 1) /(x**2 + (y + 1)**2) - 2 *x *(y + 1) *(np.sqrt(x**2 + (y + 1)**2) - 1) /(x**2 + (y + 1)**2)**(3 /2)
        dmduyx = 2 *x *(y + 1) /(x**2 + (y + 1)**2) + 2 *x *(-y - 1) *(np.sqrt(x**2 + (y + 1)**2) - 1) /(x**2 + (y + 1)**2)**(3 /2)
        dmduyy = 2 *(y + 1)**2 /(x**2 + (y + 1)**2) + 2 *(np.sqrt(x**2 + (y + 1)**2) - 1) /np.sqrt(x**2 + (y + 1)**2) + 2 *(-y - 1) *(y + 1) *(np.sqrt(x**2 + (y + 1)**2) - 1) /(x**2 + (y + 1)**2)**(3 /2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy   
    #2
    for i in range(1,10): #verified
        xi = 2 *i +1 -1
        yi = 2 *i +2 -1      

        x = us[xi]
        y = us[yi]

        dmduxx = 2 *(-x - 1) *(x + 1) *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /((x + 1)**2 + (y + 1)**2)**(3 /2) + 2 *(x + 1)**2 /((x + 1)**2 + (y + 1)**2) + 2 *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((x + 1)**2 + (y + 1)**2)
        dmduxy = 2 *(-x - 1) *(y + 1) *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /((x + 1)**2 + (y + 1)**2)**(3 /2) + 2 *(x + 1) *(y + 1) /((x + 1)**2 + (y + 1)**2)
        dmduyx = 2 *(x + 1) *(-y - 1) *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /((x + 1)**2 + (y + 1)**2)**(3 /2) + 2 *(x + 1) *(y + 1) /((x + 1)**2 + (y + 1)**2)
        dmduyy = 2 *(-y - 1) *(y + 1) *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /((x + 1)**2 + (y + 1)**2)**(3 /2) + 2 *(y + 1)**2 /((x + 1)**2 + (y + 1)**2) + 2 *(np.sqrt((x + 1)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((x + 1)**2 + (y + 1)**2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy  
        #3
    for i in range(1,10): #verified
        xi = 2 *i -1 -1
        yi = 2 *i -1

        x = us[xi]
        y = us[yi]

        dmduxx = 2 *(1 - x) *(x - 1) *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /((1 - x)**2 + (y + 1)**2)**(3 /2) + 2 *(x - 1)**2 /((1 - x)**2 + (y + 1)**2) + 2 *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((1 - x)**2 + (y + 1)**2)
        dmduxy = 2 *(1 - x) *(y + 1) *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /((1 - x)**2 + (y + 1)**2)**(3 /2) + 2 *(x - 1) *(y + 1) /((1 - x)**2 + (y + 1)**2)
        dmduyx = 2 *(x - 1) *(-y - 1) *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /((1 - x)**2 + (y + 1)**2)**(3 /2) + 2 *(x - 1) *(y + 1) /((1 - x)**2 + (y + 1)**2)
        dmduyy = 2 *(-y - 1) *(y + 1) *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /((1 - x)**2 + (y + 1)**2)**(3 /2) + 2 *(y + 1)**2 /((1 - x)**2 + (y + 1)**2) + 2 *(np.sqrt((1 - x)**2 + (y + 1)**2) - np.sqrt(2)) /np.sqrt((1 - x)**2 + (y + 1)**2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy  
        #4
    for i in range(1,31): #verified
        xi = 2 *i +20 -1
        yi = 2 *i -1
        vi = 2 *i +19 -1
        wi = 2 *i -1 -1

        x = us[xi]
        y = us[yi]
        v = us[vi]
        w = us[wi]

        dmduxx = 2 *(x - y + 1)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduxy = 2 *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1)**2 /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduxv = 2 *(v - w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduxw = 2 *(-v + w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)

        dmduyx = 2 *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1)**2 /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduyy = 2 *(-x + y - 1)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduyv = 2 *(v - w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduyw = 2 *(-v + w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)

        dmduvx = 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)
        dmduvy = 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)
        dmduvv = 2 *(-v + w) *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduvw = 2 *(-v + w)**2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w) *(v - w) /((v - w)**2 + (x - y + 1)**2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)

        dmduwx = 2 *(-v + w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduwy = 2 *(-v + w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduwv = 2 *(-v + w) *(v - w) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w)**2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduww = 2 *(-v + w)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(-v + w) *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[xi, vi] += dmduxv
        f_new[xi, wi] += dmduxw

        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy
        f_new[yi, vi] += dmduyv
        f_new[yi, wi] += dmduyw

        f_new[vi, xi] += dmduvx
        f_new[vi, yi] += dmduvy
        f_new[vi, vi] += dmduvv
        f_new[vi, wi] += dmduvw

        f_new[wi, xi] += dmduwx
        f_new[wi, yi] += dmduwy
        f_new[wi, vi] += dmduwv
        f_new[wi, wi] += dmduww       
        #5
    for i in range(1,37): #verified
        xi = 2 *i +1 + 2 *math.floor((i -1) /9) -1
        yi = 2 *i -1 + 2 *math.floor((i -1) /9) -1
        vi = 2 *i +2 + 2 *math.floor((i -1) /9) -1
        wi = 2 *i + 2 *math.floor((i -1) /9) -1

        x = us[xi]
        y = us[yi]
        v = us[vi]
        w = us[wi]

        dmduxx = 2 *(x - y + 1)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduxy = 2 *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1)**2 /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduxv = 2 *(v - w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduxw = 2 *(-v + w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)        

        dmduyx = 2 *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1)**2 /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduyy = 2 *(-x + y - 1)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduyv = 2 *(v - w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduyw = 2 *(-v + w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)

        dmduvx = 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)
        dmduvy = 2 *(-v + w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)        
        dmduvv = 2 *(-v + w) *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduvw = 2 *(-v + w)**2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w) *(v - w) /((v - w)**2 + (x - y + 1)**2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)

        dmduwx = 2 *(-v + w) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(x - y + 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduwy = 2 *(-v + w) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) *(-x + y - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2)
        dmduwv = 2 *(-v + w) *(v - w) /((v - w)**2 + (x - y + 1)**2) + 2 *(v - w)**2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) - 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)
        dmduww = 2 *(-v + w)**2 /((v - w)**2 + (x - y + 1)**2) + 2 *(-v + w) *(v - w) *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /((v - w)**2 + (x - y + 1)**2)**(3 /2) + 2 *(np.sqrt((v - w)**2 + (x - y + 1)**2) - 1) /np.sqrt((v - w)**2 + (x - y + 1)**2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[xi, vi] += dmduxv
        f_new[xi, wi] += dmduxw

        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy
        f_new[yi, vi] += dmduyv
        f_new[yi, wi] += dmduyw

        f_new[vi, xi] += dmduvx
        f_new[vi, yi] += dmduvy
        f_new[vi, vi] += dmduvv
        f_new[vi, wi] += dmduvw

        f_new[wi, xi] += dmduwx
        f_new[wi, yi] += dmduwy
        f_new[wi, vi] += dmduwv
        f_new[wi, wi] += dmduww         
        #6
    for i in range(1,28): #verified
        xi = 2 *i +21 + 2 *math.floor((i -1) /9) -1
        yi = 2 *i -1 + 2 *math.floor((i -1) /9) -1
        vi = 2 *i +22 + 2 *math.floor((i -1) /9) -1
        wi = 2 *i + 2 *math.floor((i -1) /9) -1

        x = us[xi]
        y = us[yi]
        v = us[vi]
        w = us[wi]

        dmduxx = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-x + y - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(x - y + 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)
        dmduxy = -2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-x + y - 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-x + y - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduxv = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduxw = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)        

        dmduyx = -2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(x - y + 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-x + y - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduyy = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-x + y - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-x + y - 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)
        dmduyv = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduyw = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)

        dmduvx = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduvy = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)        
        dmduvv = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(v - w + 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)
        dmduvw = -2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (x - y + 1)**2)

        dmduwx = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(x - y + 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduwy = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(-x + y - 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduwv = -2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(v - w + 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (x - y + 1)**2)
        dmduww = 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (x - y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (x - y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (x - y + 1)**2)**(3 /2) + 2 *(-v + w - 1)**2 /((v - w + 1)**2 + (x - y + 1)**2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[xi, vi] += dmduxv
        f_new[xi, wi] += dmduxw

        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy
        f_new[yi, vi] += dmduyv
        f_new[yi, wi] += dmduyw

        f_new[vi, xi] += dmduvx
        f_new[vi, yi] += dmduvy
        f_new[vi, vi] += dmduvv
        f_new[vi, wi] += dmduvw

        f_new[wi, xi] += dmduwx
        f_new[wi, yi] += dmduwy
        f_new[wi, vi] += dmduwv
        f_new[wi, wi] += dmduww          
        #7
    for i in range(1,28): #verified
        xi = 2 *i +19 + 2 *math.floor((i -1) /9) -1
        yi = 2 *i +1 + 2 *math.floor((i -1) /9) -1
        vi = 2 *i +20 + 2 *math.floor((i -1) /9) -1
        wi = 2 *i +2 + 2 *math.floor((i -1) /9) -1

        x = us[xi]
        y = us[yi]
        v = us[vi]
        w = us[wi]

        dmduxx = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-x + y + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(x - y - 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduxy = -2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-x + y + 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-x + y + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduxv = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduxw = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)        

        dmduyx = -2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(x - y - 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-x + y + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduyy = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-x + y + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-x + y + 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduyv = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduyw = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)

        dmduvx = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduvy = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(v - w + 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)        
        dmduvv = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(v - w + 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduvw = -2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (-x + y + 1)**2)

        dmduwx = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(x - y - 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduwy = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(v - w + 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(-x + y + 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduwv = -2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(v - w + 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (-x + y + 1)**2)
        dmduww = 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) /np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) + 2 *(np.sqrt((v - w + 1)**2 + (-x + y + 1)**2) - np.sqrt(2)) *(-v + w - 1) *(v - w + 1) /((v - w + 1)**2 + (-x + y + 1)**2)**(3 /2) + 2 *(-v + w - 1)**2 /((v - w + 1)**2 + (-x + y + 1)**2)

        f_new[xi, xi] += dmduxx
        f_new[xi, yi] += dmduxy
        f_new[xi, vi] += dmduxv
        f_new[xi, wi] += dmduxw

        f_new[yi, xi] += dmduyx
        f_new[yi, yi] += dmduyy
        f_new[yi, vi] += dmduyv
        f_new[yi, wi] += dmduyw

        f_new[vi, xi] += dmduvx
        f_new[vi, yi] += dmduvy
        f_new[vi, vi] += dmduvv
        f_new[vi, wi] += dmduvw

        f_new[wi, xi] += dmduwx
        f_new[wi, yi] += dmduwy
        f_new[wi, vi] += dmduwv
        f_new[wi, wi] += dmduww    
    return f_new


#print("why are there so many 0s?")
#print(dmxs2(np.arange(1,81), np.arange(1,81)))


def newton(fn, dm1, dm2, us, gs):
    print("Compute settle point using newton")  
    #Initialisation
    #set tolerance
    tol = 10**(-12)
    #Newton
    f = dm1(gs, us)
    while np.sqrt(np.dot(f,f)) > tol:
        K = dm2(gs, us)
        #first-order Taylor expansion around guess
        h = np.linalg.solve(K, -f) ##mistake here K does not have unique solution
        us = us + h
        f = dm1(gs, us)
    #completion
    u_star = us
    m_star = fn(gs, u_star)
    print("Minimum Value of model4a Function:", m_star)
    print("Optimal u:", u_star)  


new_g = np.zeros(80)  
new_g[61] = 1 #62
new_g[78] = 1 #79  
newton(model4a, gradient4a, hessian4a, np.zeros(80), new_g)    


def gradient_decent(fn, dm, us):    #initial guess for u and tolerance
    #parameters, forces
    paramgs = np.zeros(80)
    paramgs[61] = 1 #62
    paramgs[78] = 1 #79
    #step size
    alpha = 0.04 

    #initial value
    m_new = fn(paramgs,us)
    #dummy value
    m_old = 10 **100

    #gradient decent
    while m_new < m_old:

        m_old = m_new
        #calc gradient and invert it's direction
        f = dm(paramgs, us)
        h = -f
        #multiply inverted gradient by step size <1 to move in a reclining direction
        alpha_h = h * alpha #helper
        us = us + alpha_h
        m_new = fn(paramgs, us)

    m_star = m_old #m of the last iteration was optimal
    u_star = us -alpha *h    #u of the last iteration was optimal
    print("Minimum Value of model4a Function:", m_star)
    print("Optimal u:", u_star)   


#gradient_decent(model4a, dmxs1, np.zeros(80))