from functions import *
import math as m
import numpy as np
import matplotlib.pyplot as plt


def P(x,xi):
    def L(x,j,xi):
        l=1
        for i in range(len(xi)):
            if j != i:
                l=l*(x-xi[i])
        return l
    s=0
    for i in range(len(xi)):
        s=s+func_Besi(xi[i],0)*(L(x,i,xi)/L(xi[i],i,xi))
    return s
def graf(n,r):
    x=np.linspace(0, 10, n)
    y = [func_Besi(ri, 0) for ri in r]
    z = [P(ri, x) for ri in r]
    t=abs(np.array(y)-np.array(z))
    plt.figure(figsize=(10, 8))
    plt.plot(r, t, 'b-', linewidth=2, label='J₀(x)-Pn(x)')
    plt.xlabel('x', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

def multigraph(n_list,r):
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
    plt.figure(figsize=(10, 8))
    w=0
    for n in n_list:
        x=np.linspace(0, 10, n)
        y = [func_Besi(ri, 0) for ri in r]
        z = [P(ri, x) for ri in r]
        t=abs(np.array(y)-np.array(z))
        color=colors[w]
        plt.plot(r, t, color=color, linewidth=2, label=f'J₀(x)-Pn(x) число узлов n={n}')
        w=w+1
    plt.xlabel('x', fontsize=12)
    plt.ylabel('Значения модуля ошибки', fontsize=12)
    plt.title('Разные ошибки в зависимости от разного числа узлов n', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()





x=np.linspace(0, 10, 48)
y = [func_Besi(xi, 0) for xi in x]
z = [P(xi, x) for xi in x]
N_list=[3,5,7]


multigraph(N_list,x)
