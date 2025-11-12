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
x=np.linspace(0, 2*np.pi, 20)
J = [func_Besi(xi, 1) for xi in x] 
ddJ = [dJ(xi, 0) for xi in x] 
sum_values = [d + j for d, j in zip(ddJ, J)]
plt.figure(figsize=(10, 8))
plt.plot(x, J, 'b-', linewidth=2, label='J₁(x)')
plt.plot(x, ddJ, 'r--', linewidth=2, label='J₀\'(x)')
plt.plot(x, sum_values, 'g--', linewidth=2, label='J₀\'(x)+J₁(x)')
plt.xlabel('x', fontsize=12)
plt.ylabel('Значения функций', fontsize=12)
plt.title('Функции Бесселя J₁(x) и производная J₀\'(x)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xlim(0, 2*np.pi)
plt.tight_layout()
plt.savefig('Демонстрация_графическая_1.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 8))
plt.plot(x, sum_values, 'b-', linewidth=2, label='J₀\'(x)+J₁(x)')
plt.xlabel('x', fontsize=12)
plt.ylabel('Значения функции J₀\'(x)+J₁(x)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, 2*np.pi)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('Демонстрация_графическая_2.png', dpi=300, bbox_inches='tight')
plt.show()

n = [2, 4, 8, 16,32,64,128]
integral_trap=[abs(integral_trapec(sin,0,m.pi,ni)-2) for ni in n]
integral_simps=[abs(integral_simpson(sin,0,m.pi,ni)-2) for ni in n]
plt.figure(figsize=(10, 8))
plt.grid(True) 
plt.plot(n, integral_trap, 'b-', linewidth=2, label='Метод трапеций')
plt.plot(n, integral_simps, 'g-', linewidth=2, label='Метод симпсона')
plt.legend(fontsize=12)
plt.yscale('log') 
plt.ylabel('Абсолютная ошибка (на примере интеграла синуса от 0 до pi)', fontsize=12)
plt.xlabel('Число разбиений n', fontsize=12)
plt.tight_layout()
plt.savefig('Демонстрация_графическая_3.png', dpi=300, bbox_inches='tight')
plt.show()
print(sin(0))
print(integral_trapec(sin,0,m.pi,2))