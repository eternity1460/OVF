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
#t-индикатор ГУ (Дирехле="D", Нейман= "N") 
# "D":{y(-pi/2)=a, y(pi/2)=b} 
# "N":{y'(-pi/2)=a, y'(pi/2)=b}
def creat_matrix(n,t,a,b):
    h=m.pi/(n-1)
    x=np.linspace(-m.pi/2,m.pi/2,n)
    y=np.zeros(n)
    d=np.zeros(n)
    A = np.zeros((n, n))
    for i in range(n-1):
        d[i]=h*h*m.cos(x[i])
        A[i,i]=-2
        A[i,i+1]=1
        A[i+1,i]=1
    d[n-1]=h*h*m.cos(x[n-1])
    A[n-1,n-1]=-2
    if (t=="D"):
        A[0,0]=1
        A[0,1]=0
        d[0]=a
        A[n-1,n-2]=0
        A[n-1,n-1]=1
        d[n-1]=b
        y=tri_diogonal(A,d)
        plt.plot(x, y, 'b-', linewidth=1, label=f'Численное Решение y"=cos(x), c ГУ Дирехле:\n y(-pi/2)={a}\n y(pi/2)={b}\n')
        return y
    if (t=="N"):
        if(b-a!=2):
            print('ГУ для N не подходит')
            return
        A[0,0]=-2
        A[0,1]=2
        d[0]=d[0]+2*h*a
        A[n-1,n-1]=-1.99
        A[n-1,n-2]=2
        d[n-1]=d[n-1]-2*h*b
        y=tri_diogonal(A,d)
        plt.plot(x, y, 'g-', linewidth=1, label=f'Чсиленное Решение y"=cos(x), c ГУ Неймана:\n dy/dx(-pi/2)={a}\n dy/dx(pi/2)={b}\n')
        return y


#a1*y(-pi/2)+b1*y'(-pi/2)=c1
#a2*y(pi/2)+b2*y'(pi/2)=c2
def smesh_GY(n,a1,b1,c1,a2,b2,c2):
    h=m.pi/(n-1)
    x=np.linspace(-m.pi/2,m.pi/2,n)
    y=np.zeros(n)
    d=np.zeros(n)
    A = np.zeros((n, n))
    for i in range(n-1):
        d[i]=h*h*m.cos(x[i])
        A[i,i]=-2
        A[i,i+1]=1
        A[i+1,i]=1
    d[n-1]=h*h*m.cos(x[n-1])
    A[n-1,n-1]=-2
    A[0,0]=-b1/h+a1
    A[0,1]=b1/h
    d[0]=c1
    A[n-1,n-1]=-b2/h+a2
    A[n-1,n-2]=b2/h
    d[n-1]=c2
    y=tri_diogonal(A,d)
    plt.plot(x, y, 'r-', linewidth=1, label=f'Чсиленное Решение y"=cos(x), cо смешанным ГУ:\n {a1}*y(-pi/2)+{b1}*dy/dx(-pi/2)={c1}\n {a2}*y(pi/2)+{b2}*dy/dx(pi/2)={c2}')
    return y



#B = np.array([[4,1,0,0,0],[1,5,2,0,0],[0,2,6,1,0],[0,0,1,3,2],[0,0,0,2,4]], dtype=float)
#v = np.array([6,17,26,25,28], dtype=float)
#x = np.linalg.solve(B, v)
#print(x)
#tri_diogonal(B,v)
plt.figure(figsize=(10, 8))
creat_matrix(100,"D",1,-0.5)
creat_matrix(100,"N",-2,0) #В случае неймана будет работать тока при y'(pi/2)-y'(-pi/2)=2 Так же для однозначности функции y(pi/2)=0
smesh_GY(100,1,1,0,1,0,0)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Решение дифура методом прогонки', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('ГРафик_для_задачи_9.png', dpi=300, bbox_inches='tight')
plt.show() 
   



