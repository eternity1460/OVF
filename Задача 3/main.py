import math
import numpy as np
import matplotlib.pyplot as plt


exact = math.atan(1) - math.atan(-1) 
def print_orders(method_func, method_name):
    print(f"\n{method_name}:")
    prev_error = None
    for n in [10, 20, 40, 80, 160]:
        approx = method_func(func, -1, 1, n)
        error = abs(exact - approx)
        if prev_error is not None:
            order = math.log(prev_error / error) / math.log(n / (n//2))
            print(f"n={n}: ошибка={error:.2e}, порядок={order:.2f}")
        else:
            print(f"n={n}: ошибка={error:.2e}")
        prev_error = error

def func(x):
    return 1/(1+x*x)

def integral_low(f,a,b,n):
    dx=(b-a)/n
    s=0
    for i in range(n):
        s=f(a+dx*i)*dx+s
    return s

def integral_high(f,a,b,n):
    dx=(b-a)/n
    s=0
    for i in range(n):
        s=f(a+dx*(i+1))*dx+s
    return s
def integral_mid(f,a,b,n):
    dx=(b-a)/n
    s=0
    for i in range(n):
        s=f(a+dx*(i+0.5))*dx+s
    return s
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
def print_orders(method_func, method_name):
    print(f"\n{method_name}:")
    prev_error = None
    for n in [10, 20, 40, 80, 160]:
        approx = method_func(func, -1, 1, n)
        if approx is None:  
            continue
        error = abs(exact - approx)
        if prev_error is not None:
            order = math.log(prev_error / error) / math.log(n / (n//2))
            print(f"n={n}: ошибка={error:.2e}, порядок={order:.2f}")
        else:
            print(f"n={n}: ошибка={error:.2e}")
        prev_error = error
def plot_all_errors():
    n_values = [10, 20, 40, 80, 160, 320]
    
    methods = {
        'Левые': integral_low,
        'Правые': integral_high,
        'Средние': integral_mid,
        'Трапеции': integral_trapec,
        'Симпсон': integral_simpson
    }
    
    plt.figure(figsize=(12, 8))
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(methods)))
    
    for i, (name, method) in enumerate(methods.items()):
        errors = []
        valid_n = []
        
        for n in n_values:
            if name == 'Симпсон' and n % 2 != 0:
                continue
                
            approx = method(func, -1, 1, n)
            if approx is not None:
                error = abs(exact - approx)
                errors.append(error)
                valid_n.append(n)
        
        plt.plot(valid_n, errors, 
                marker='o',
                color=colors[i],
                linestyle='-',
                linewidth=2,
                markersize=6,
                label=name)
    
    plt.xlabel('n')
    plt.ylabel('Ошибка')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


print('Интеграл методом левых прямоугольников',integral_low(func,-1,1,10))
print('Интеграл методом правых прямоугольников',integral_high(func,-1,1,10))
print('Интеграл методом средних',integral_mid(func,-1,1,10))
print('Интеграл методом трапеций',integral_trapec(func,-1,1,10))
print('Интеграл методом Симпсона',integral_simpson(func,-1,1,10))
print_orders(integral_low, "Левые прямоугольники")
print_orders(integral_high, "Правые прямоугольники")
print_orders(integral_mid, "Средние прямоугольники")
print_orders(integral_trapec, "Трапеции")
print_orders(integral_simpson, "Симпсон")
plot_all_errors()