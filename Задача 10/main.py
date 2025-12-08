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

#T-шаг сетки по времени, N-число узлов по координате, n-число временных узлов 
def creat_MATRIX(T,N,n):
    h=1/(N-1)
    t=np.linspace(0,T*(n-1),n)
    x=np.linspace(0,1,N)
    u=np.zeros((n, N))
    #создаем матрицу A
    B=np.zeros((N-2, N-2))
    for i in range(N-3):
        B[i,i]=1+T/(h*h)
        B[i,i+1]=-0.5*T/(h*h)
        B[i+1,i]=-0.5*T/(h*h)
    B[N-3,N-3]=1+T/(h*h)
    v=np.zeros((N-2))
    #тут начинаем основную прогонку 
    for i in range(N):
        u[0,i]=m.sin(m.pi*x[i])
    for i in range(n-1):
        for k in range(N-2):
            v[k]=u[i,k+1]+T*((u[i,k+2]-2*u[i,k+1]+u[i,k])/(2*h*h))
        y = tri_diogonal(B.copy(), v.copy())
        u[i+1, 1:-1] = y
    return u
#U-наша матрица решений, T-шаг сетки по времени, N-число узлов по координате, n-число временных узлов, MAIN-какую точку по врмени будем отрисововать варианты (0,1,2,n-1)
def graf_2d(u,T,N,n,MAIN):
    h=1/(N-1)
    t=np.linspace(0,T*(n-1),n)
    x=np.linspace(0,1,N)
    MOMENT=T*MAIN
    plt.figure(figsize=(10, 6))
    plt.plot(x, u[MAIN, :] , 'b-', linewidth=2.5, label=f'U(x, t={MOMENT:.2f})\n Число шагов N по координате = {N}\n Шаг по координате h = {h:.2f} \nЧисле шогов n по времени = {n}\n Шаг по времнеи τ ={T}')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('u', fontsize=12)
    plt.title('Решение уравнения теплопроводности', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('ГРафик_для_задачи_10.png', dpi=300, bbox_inches='tight')
    plt.show()
def graf_3d(u, T, N, n):   
    h = 1.0 / (N - 1) 
    x = np.linspace(0, 1, N)  
    t = np.linspace(0, T*(n-1), n) 
    X, T_grid = np.meshgrid(x, t)
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, T_grid, u, 
                          cmap='viridis',      # цветовая карта
                          alpha=0.8,           # прозрачность
                          linewidth=0.1       # ширина линий сетки
                          )    
    ax.set_xlabel('Координата x', fontsize=12, labelpad=10)
    ax.set_ylabel('Время t', fontsize=12, labelpad=10)
    ax.set_zlabel('U(x,t)', fontsize=12, labelpad=10)
    title = (f'Решение уравнения теплопроводности\n'
             f'N={N}, h={h:.3f}, n={n}, τ={T:.3f}\n'
             f'Общее время: {T*(n-1):.2f}')
    ax.set_title(title, fontsize=14, pad=20)
    fig.colorbar(surf, shrink=0.5, aspect=10, pad=0.1, label='Значение U(x,t)')
    ax.view_init(elev=30, azim=-45)
    ax.grid(True, alpha=0.3)
    #ax.contourf(X, T_grid, u, zdir='y', offset=0, cmap='viridis', alpha=0.3)   
    plt.tight_layout()
    plt.savefig('3D_график_теплопроводности.png', dpi=300, bbox_inches='tight')
    plt.show()
def START_2d(T,N,n,MAIN):
    L=creat_MATRIX(T,N,n)
    graf_2d(L,T,N,n,MAIN)
def START_3d(T,N,n):
    L=creat_MATRIX(T,N,n)
    graf_3d(L,T,N,n)



        
START_2d(0.01,200,100,20)
START_3d(0.01,200,30)    





        

