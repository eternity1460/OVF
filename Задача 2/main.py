import math as m
import numpy as np
import matplotlib.pyplot as plt

#a=4
#U0=10


def func_for_E(E):
    U0=10
    a=4
    return (m.sqrt(2*(U0 + E)) * m.tan(a * m.sqrt(2*(U0 + E))) - m.sqrt(-2*E))

def proizv_func(f,x):
    h=1e-6
    return (f(x + h) - f(x - h)) / (2 * h)

def prost_iter(f,h,e,x0):#h-это лямда в методе корректирующего множителя
    t=e
    g=0
    while t!=1:
        g=g+1
        t=t*10
    while True:
        x_old = x0
        x0 = x0 - h * f(x0)
        if m.fabs(x0 - x_old) < e:
            break
    return round(x0, g)

def method_nuton(f,df,x0,e):
    t=e
    g=0
    while t!=1:
        g=g+1
        t=t*10
    while True:
        x_old = x0
        x0 = x0 - (f(x0)/df(f,x0))
        if m.fabs(x0 - x_old) < e:
            break
    return round(x0, g)

def deh_method(f,e,b,a):
    #e-требуемая тончость
    #[a,b]-интервал
    t=e
    g=0
    while t!=1:
        g=g+1
        t=t*10


    for i in range(1,m.ceil(m.log2((b-a)/e))):
        if f((b+a)*0.5)*f(a)<=0:
            b=0.5*(b+a)
        else:
            a=0.5*(b+a)
    return round((a+b)*0.5, g)
print('Метод дихотомии: E0 =',deh_method(func_for_E,0.00001,0,-2))
print('Метод простых итераций: E0 =',prost_iter(func_for_E,0.1,0.00001,-2))
print('Метод Ньютона: E0 =',method_nuton(func_for_E,proizv_func,-2,0.0001))