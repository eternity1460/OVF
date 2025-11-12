import math as mpy
import numpy as np
import matplotlib.pyplot as plt


#загатовка, вектор функция f=(f1,f2), правая часть дифура 
def func_vect(u):
    a=10
    b=2
    c=2
    d=10
    x, y = u
    f1=a*x-b*x*y
    f2=c*x*y-d*y
    return np.array([f1,f2])
def method_kyte_2(n,h,x0,y0,f,alpha):
    x = np.zeros((n, 2))
    dx = np.zeros((n, 2))
    x[0] = [x0, y0]
    for i in range(n-1):
         x[i+1]=x[i]+h*((1-alpha)*f(x[i])+alpha*f(x[i]+(h/(2*alpha))*f(x[i])))
    plt.plot(x[:,0], x[:,1], 'g-', linewidth=1, label=f'Фазовая траектория диференциального уравнения Хищник-Жертва, (x(0),y(0))=({x0},{y0})')
    print(x)
plt.figure(figsize=(10, 8))
method_kyte_2(2000,0.003,3,2,func_vect,0.75)
plt.scatter(5, 5, color='red', s=40, label='Точка равновесия популяции (5,5)')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Решение дифурчика Хищник-Жертва', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('ГРафик_для_задачи_7.png', dpi=300, bbox_inches='tight')
plt.show() 