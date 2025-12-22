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
def potencial(x):
    return(1/2*x*x)
#(-L;L)-интревал по x
#N-число точка на это интервале
#psi0-начлаьное приближение вектора волновой функции задается просто как psi0=(1,1,1,...,1), конечно сразу нормируется 
#U-наш потенциал
#e-точность СХОДИМОСТИ метода обратных итераций на волновую функцию, ВНИМАНИЕ!!! это не точнсть на волновую функцию (см. Точностный критерий.jpg) влияет еще L и N
def reshenie(L,U,N,e):
    h=2*L/(N-1)
    psi0=np.ones(N)
    norm0 = np.sqrt(np.sum(psi0**2) * h)  
    psi0 = psi0 / norm0
    psi_old=np.zeros((N))
    psi_res=np.zeros((N))
    psi_res=psi0
    H=np.zeros((N, N))
    x=np.linspace(-L,L,N)
    for i in range (N-1):
        H[i,i]=1/(h*h)+U(x[i])
        H[i,i+1]=-1/(2*h*h)
        H[i+1,i]=-1/(2*h*h)
    H[N-1,N-1]=1/(h*h)+U(x[N-1])
    while (1-np.abs(np.sum(psi_old * psi_res) * h)>e):
        psi_old=psi_res
        psi_res=tri_diogonal(H.copy(),psi_old.copy())
        norm_res = np.sqrt(np.sum(psi_res**2) * h)
        psi_res = psi_res / norm_res
    H_psi = np.dot(H,psi_res)  
    numerator = np.dot(psi_res, H_psi)
    denominator = np.dot(psi_res, psi_res)
    E0 = numerator / denominator
    plt.figure(figsize=(10, 6))
    t=np.linspace(-L,L,100000)
    y=[np.pi**(-0.25) * np.exp(-ti**2 / 2) for ti in t]
    plt.plot(x, psi_res , 'b-', linewidth=2.5,alpha=0.6, label=f'Численное решение ψ0(x)\n Интервал x: ({-L},{L})\n Число точек N={N}\n Точность сходимости мтеода обратных итераций e = {e}\n E0={E0:.3f}')
    plt.plot(t, y , 'g--', linewidth=2.5,alpha=0.6, label=f'Аналитическое решение ψ0(x)')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('ψ', fontsize=12)
    plt.title('Решение уравнения Шрёдингера', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('ГРафик_для_задачи_11.png', dpi=300, bbox_inches='tight')
    plt.show()
    return(E0)



print(reshenie(10,potencial,1000,0.00001))