import math as m
import numpy as np
import matplotlib.pyplot as plt



def func(x):
    return (-x)

def method_Elera(n,f,x0,y0,a,b):
    h=(b-a)/(n-1)
    t=np.linspace(a, b, n)
    x=np.empty(n)
    x[0]=y0
    for i in range(n-1):
        x[i+1]=x[i]+h*f(x[i])
    plt.plot(t, x, 'b-', linewidth=1, label=f'Метод Эйлера, число узлов n={n}')
   
def method_kyte_2(n,f,x0,y0,a,b,alpha):
    h=(b-a)/(n-1)
    t=np.linspace(a, b, n)
    x=np.empty(n)
    x[0]=y0
    for i in range(n-1):
        x[i+1]=x[i]+h*((1-alpha)*f(x[i])+alpha*f(x[i]+(h/(2*alpha))*f(x[i])))
    plt.plot(t, x, 'g-', linewidth=1, label=f'Метод Рунге-Куты 2 порядка, число узлов n={n}')
    
def method_kyte_4(n,f,x0,y0,a,b):
    h=(b-a)/(n-1)
    t=np.linspace(a, b, n)
    x=np.empty(n)
    x[0] = y0 
    for i in range(n-1):
        k1=f(x[i])
        k2=f(x[i]+h/2*k1)
        k3=f(x[i]+h/2*k2)
        k4=f(x[i]+h*k3)
        x[i+1]=x[i]+h/6*(k1+2*k2+2*k3+k4)
    plt.plot(t, x, 'r-', linewidth=1, label=f'Метод Рунге-Куты 4 порядка точности, число узлов n={n}')
   


t=np.linspace(0, 3, 100)
x=[m.exp(-ti) for ti in t]
plt.figure(figsize=(10, 8))  
method_Elera(5,func,0,1,0,3) 
method_kyte_2(5,func,0,1,0,3,0.75)     
method_kyte_4(5,func,0,1,0,3) 
plt.plot(t, x, 'y-', linewidth=1, label='Аналитическое решение x=exp(-t)') 
plt.xlabel('t', fontsize=12)
plt.ylabel('x', fontsize=12)
plt.title('x(t)-решения диференциального уравнения dx/dt=-x', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('ГРафик_для_задачи_6.png', dpi=300, bbox_inches='tight')
plt.show() 






