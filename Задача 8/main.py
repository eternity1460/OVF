import math as m
import numpy as np
import matplotlib.pyplot as plt



def func_vect(y):
    u, v = y
    f1=998*u+1998*v
    f2=-999*u-1999*v
    return np.array([f1,f2])
def shema_1(n,h,f,u0,v0):
    y=np.zeros((n, 2))
    y[0]=[u0,v0]
    t=np.linspace(0,n*h,n)
    for i in range(n-1):
        y[i+1]=y[i]+h*f(y[i])
    plt.plot(t, y[:,0], 'g-', linewidth=1, label=f'U(t) методом явной схемы, (u(0))=({u0}), h={h}')
    plt.plot(t, y[:,1], 'b-', linewidth=1, label=f'V(t) методом явной схемы, (v(0))=({v0}), h={h}')

def shema_2(n,h,u0,v0): #тут вместо функции f задаем матрицу этой функции прям внутри исполняемой питоновской функции
    A = np.array([[998, 1998], [-999, -1999]])
    I = np.eye(2)
    t=np.linspace(0,n*h,n)
    main_matrix= I + 0.5 * h * A
    inv_matrix = np.linalg.inv(I - 0.5 * h * A)
    mnoj=np.dot(inv_matrix, main_matrix)
    y=np.zeros((n, 2))
    y[0]=[u0,v0]
    for i in range(n-1):
        y[i+1] = np.dot(mnoj, y[i])
    plt.plot(t, y[:,0], 'g-', linewidth=1, label=f'U(t) методом полунеявной схемы, (u(0))=({u0}), h={h}')
    plt.plot(t, y[:,1], 'b-', linewidth=1, label=f'V(t) методом полунеявной схемы, (v(0))=({v0}), h={h}')


def shema_3(n,h,u0,v0): #тут вместо функции f задаем матрицу этой функции прям внутри исполняемой питоновской функции
    A = np.array([[998, 1998], [-999, -1999]])
    I = np.eye(2)
    t=np.linspace(0,n*h,n)
    inv_matrix = np.linalg.inv(I - h * A)
    y=np.zeros((n, 2))
    y[0]=[u0,v0]
    for i in range(n-1):
        y[i+1] = np.dot(inv_matrix, y[i])
    plt.plot(t, y[:,0], 'g-', linewidth=1, label=f'U(t) методом неявной схемы, (u(0))=({u0}), h={h}')
    plt.plot(t, y[:,1], 'b-', linewidth=1, label=f'V(t) методом неявной схемы, (v(0))=({v0}), h={h}')


plt.figure(figsize=(10, 8))
t=np.linspace(0,6,100)
u=[2*m.exp(-ti)-m.exp(-1000*ti) for ti in t]
v=[-m.exp(-ti)+m.exp(-1000*ti) for ti in t]
plt.plot(t, u, 'r-', linewidth=1, label='U(t) аналитическое решение, (u(0))=(1)')
plt.plot(t, v, 'y-', linewidth=1, label='V(t) аналитическое решение, (v(0))=(0)')
shema_1(1000,0.001,func_vect,1,0) #h<0.002
#shema_2(60,0.1,1,0)
#shema_3(60,0.1,1,0)
plt.xlabel('t', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.title('Решение дифурча', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show() 







