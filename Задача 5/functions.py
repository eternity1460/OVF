import math as m
import numpy as np
import matplotlib.pyplot as plt


def func_Besi(x,n):
    def integrand(t):
        return np.cos(n * t - x * np.sin(t))
    
    return (1/m.pi) * integral_simpson(integrand, 0, m.pi,  200)
def sin(x):
    return m.sin(x)
def dJ(x,n):
    h=1e-6
    return (func_Besi(x + h,n) - func_Besi(x - h,n)) / (2 * h)
def creat_graf(x,y1):
    plt.figure(figsize=(10, 8))
    plt.plot(x, y1, 'b-', linewidth=2)
    plt.xlabel('x', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()


def func(x,m,t):
    return np.cos(m * t - x * np.sin(t))
def integral_trapec(f,a,b,n):
    dx=(b-a)/n
    s=0
    for i in range(n):
        s=(f(a+(i+1)*dx)+f(a+i*dx))/2*dx+s
    return s

def integral_simpson(f,a,b,n):
    if n% 2 == 0 :
        dx=(b-a)/n
        s=0
        for i in range(0, n, 2):
            s=(2*dx)/6*(f(a+i*dx)+4*f(a+(i+1)*dx)+f(a+(i+2)*dx))+s
        return s
    else:
        print('N должно быть четным!!!!')
