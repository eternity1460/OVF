import math as m
import numpy as np
import matplotlib.pyplot as plt


def tri_diogonal(A,d):
    n = len(A) #вычисляем ремзерность матрицы 
    y=np.zeros(n)
    if (n!=len(d)):
        print('Несовподение размерностей A и D')
        return
    for i in range(n-1):
        e=A[i+1,i]/A[i,i]
        A[i+1,i]=0
        A[i+1,i+1]=A[i+1,i+1]-e*A[i,i+1]
        d[i+1]=d[i+1]-e*d[i]
    y[n-1]=d[n-1]/A[n-1,n-1]
    for i in reversed(range(n-1)):
        y[i]=(d[i]-A[i,i+1]*y[i+1])/A[i,i]
    return y
#Наша функция U(x,0)
def U0(x):
    return np.exp(-(x*x)/2)


#n-Число точек по времени 
#N-Число точек по координате 
#f-это наша функция U(x,0)
def shema_LAXSA(n,N,f):
    T=1/(n-1) #шаг по времени 
    x=np.linspace(-5,10,N)
    t=np.linspace(0,1,n)
    h=15/(N-1) #шаг по координате
    U=np.zeros((n, N)) # матрица решений строки-время стоблцы-координаты
    for i in range(N):
        U[0,i]=f(x[i])
    for i in range(n):
        U[i,0]=f(x[0])
        U[i,N-1]=f(x[N-1])
    for k in range(n-1):
        for i in range(1, N-1):
            u_left=U[k,i-1]
            u_right=U[k,i+1]
            avg=(u_right + u_left)/2
            flux=(T/(4*h))*(u_right*u_right-u_left*u_left)
            U[k+1,i]=avg-flux
    return U,x
def linel_upwind(n,N,f):
    T=1/(n-1) #шаг по времени 
    x=np.linspace(-5,10,N)
    t=np.linspace(0,1,n)
    v=np.zeros((N))
    B=np.eye(N)
    h=15/(N-1) #шаг по координате
    U=np.zeros((n, N)) # матрица решений строки-время стоблцы-координаты
    for i in range(N):
        U[0,i]=f(x[i])
    for i in range(n-1):
        U[i,0]=f(x[0])
        U[i,N-1]=f(x[N-1])
    for i in range(n-1):
        for k in range(N):
            v[k]=U[i,k]
        v[0] = U[0, 0] 
        v[-1] = U[0, -1]
        for k in range(N-1):
            B[k+1,k]=-T/h*v[k+1]
            B[k+1,k+1]=1+T/h*v[k+1]
        U[i+1,:]=tri_diogonal(B,v)
    return U,x


def plot_reshenie_1(i,n,N):
    """
    Строит график неявной функции через contour
    """
    # Создаём сетку
    x = np.linspace(-5, 10, 4000)
    y = np.linspace(0, 1.2, 4000)  # y от 0 до 1.2 (u не может быть >1 и <0)
    X, Y = np.meshgrid(x, y)

    (A,Z)=shema_LAXSA(n,N,U0)
    T=1/(n-1)
    h=15/(N-1)
    t=i*T
    # Уравнение: F(x,y) = y - exp(-(x - y*t)^2/2) = 0
    F = Y - np.exp(-(X - Y*t)**2 / 2)
    
    plt.figure(figsize=(10, 6))
    # Рисуем линию уровня F=0
    contour = plt.contour(X, Y, F, levels=[0], colors='red', linewidths=2.5)
    plt.plot(Z, A[i,:] , 'g--', linewidth=2.5,alpha=0.6,label=f'Численное решение U(x,t) для точки t={t:.2f} \n Шаг по координате h={h:.3f}\n Шаг по времени τ={T:.3f}\n CFL=τ/h={T/h:.2f}')
    plt.plot(0, 0 , 'red', linewidth=2.5,label=f'Анлитическое решение U(x,t) для точки t={t:.2f}')
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('U', fontsize=12)
    plt.title('Решени уравнения Xопфа схемой Лакса-Фридриха', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.ylim(0, 1.1)
    plt.savefig('Схема Лакса-Фридриха.png', dpi=300, bbox_inches='tight')
    plt.show()
def plot_reshenie_2(i,n,N):
    """
    Строит график неявной функции через contour
    """
    # Создаём сетку
    x = np.linspace(-5, 10, 4000)
    y = np.linspace(0, 1.2, 4000)  # y от 0 до 1.2 (u не может быть >1 и <0)
    X, Y = np.meshgrid(x, y)

    (A,Z)=linel_upwind(n,N,U0)
    T=1/(n-1)
    h=15/(N-1)
    t=i*T
    # Уравнение: F(x,y) = y - exp(-(x - y*t)^2/2) = 0
    F = Y - np.exp(-(X - Y*t)**2 / 2)
    
    plt.figure(figsize=(10, 6))
    # Рисуем линию уровня F=0
    contour = plt.contour(X, Y, F, levels=[0], colors='red', linewidths=2.5)
    plt.plot(Z, A[i,:] , 'g--', linewidth=2.5,alpha=0.6,label=f'Численное решение U(x,t) для точки t={t:.2f} \n Шаг по координате h={h:.3f}\n Шаг по времени τ={T:.3f}\n CFL=τ/h={T/h:.2f}')
    plt.plot(0, 0 , 'red', linewidth=2.5,label=f'Анлитическое решение U(x,t) для точки t={t:.2f}')
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('U', fontsize=12)
    plt.title('Решени уравнения Xопфа линеаризованной схемой upwind', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.ylim(0, 1.1)
    plt.savefig('Схема upwind.png', dpi=300, bbox_inches='tight')
    plt.show()
def plot_reshenie_vmeste(i,n,N):
    """
    Строит график неявной функции через contour
    """
    # Создаём сетку
    x = np.linspace(-5, 10, 4000)
    y = np.linspace(0, 1.2, 4000)  # y от 0 до 1.2 (u не может быть >1 и <0)
    X, Y = np.meshgrid(x, y)

    (A,Z)=linel_upwind(n,N,U0)
    (A1,Z1)=shema_LAXSA(n,N,U0)
    T=1/(n-1)
    h=15/(N-1)
    t=i*T
    # Уравнение: F(x,y) = y - exp(-(x - y*t)^2/2) = 0
    F = Y - np.exp(-(X - Y*t)**2 / 2)
    
    plt.figure(figsize=(10, 6))
    # Рисуем линию уровня F=0
    contour = plt.contour(X, Y, F, levels=[0], colors='red', linewidths=2.5)
    plt.plot(Z, A[i,:] , 'g--', linewidth=2.5,alpha=0.6,label=f'Схема upwing для точки t={t:.2f} \n Шаг по координате h={h:.3f}\n Шаг по времени τ={T:.3f}\n CFL=τ/h={T/h:.2f}')
    plt.plot(Z1, A1[i,:] , 'b--', linewidth=2.5,alpha=0.6,label=f'Схема Лакса-Фридриха с аналогичными параметрами')
    plt.plot(0, 0 , 'red', linewidth=2.5,label=f'Анлитическое решение U(x,t) для точки t={t:.2f}')
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('U', fontsize=12)
    plt.title('Решени уравнения Xопфа линеаризованной схемой upwind', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.ylim(0, 1.1)
    plt.savefig('Две схемы вместе.png', dpi=300, bbox_inches='tight')
    plt.show()    
    


plot_reshenie_1(44,100,1000)

plot_reshenie_2(198,200,4000)

plot_reshenie_vmeste(99,100,1400)






