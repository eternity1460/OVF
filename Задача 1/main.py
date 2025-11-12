import math
import numpy as np

def machine_epsilon32():
    epsilon = np.float32(1.0)
    while np.float32(1.0) + epsilon * np.float32(0.5) > np.float32(1.0):
        epsilon *= np.float32(0.5)
    return epsilon

def machine_epsilon64():
    epsilon = np.float64(1.0)
    while np.float64(1.0) + epsilon * np.float64(0.5) > np.float64(1.0):
        epsilon *= np.float64(0.5)
    return epsilon

def min_to_max():
    summ=0
    for i in range(10000):
        summ=summ+(pow(-1,i+1)/(i+1))
    return summ
def max_to_min():
    summ=0
    for i in reversed(range(10000)):
        summ=summ+(pow(-1,i+1)/(i+1))
    return summ
def min_to_max_comp():
    summ1=0
    summ2=0
    for i in range(10000):
        t=pow(-1,i+1)/(i+1)
        if(t>=0):
            summ1=summ1+(pow(-1,i+1)/(i+1))

        if(t<0):
            summ2=summ2+(pow(-1,i+1)/(i+1))
    return summ1+summ2
def max_to_min_comp():
    summ1=0
    summ2=0
    for i in reversed(range(10000)):
        t=pow(-1,i+1)/(i+1)
        if(t>=0):
            summ1=summ1+(pow(-1,i+1)/(i+1))

        if(t<0):
            summ2=summ2+(pow(-1,i+1)/(i+1))
    return summ1+summ2


epsilon_float32 = machine_epsilon32()
print('Машинное  ε для типа float32(единичная точность) = ',epsilon_float32)
epsilon_float64 = machine_epsilon64()
print('Машинное  ε для типа float64(двойная точность) = ',epsilon_float64)
print('От 1 до 10000=',min_to_max())
print('От 10000 до 1=',max_to_min())
print('От 1 до 10000, по группам=',min_to_max_comp())
print('От 10000 до 1, по группам=',max_to_min_comp())