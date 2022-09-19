import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def bisection_method(func, a, b, error_accept):
    i = 1
    def f(x):
        f = eval(func)
        return f 
    
    error = abs(b-a)
    data = [['iterasi', 'x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)']]
    while error > error_accept:
        c = (b+a)/2
        data.append([i,a,b,c,f(a),f(b),f(c)])
        i = i + 1
        if f(a) * f(b) >= 0:
            print("No root or multiple roots present")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b-a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b-a)

        else:
            print("Error happens")
            quit()

    
    print(tabulate(data, headers="firstrow", tablefmt="github"))

    print(f"The lower boundary is {a} and upper boundary is {b}")

function = input("function : ")
a = input("lower root boundary: ")
b = input("upper root boundary: ")
acceptable_error = input("acceptable error level: ")

x = np.linspace(-10,10,num = 1000)
y = eval(function)
plt.plot(x, y)
plt.show()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

bisection_method(function, float(a), float(b), float(acceptable_error))