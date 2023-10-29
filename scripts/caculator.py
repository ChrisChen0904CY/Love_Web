import math

def trapezoidal_rule(f, a, b, n):
    h = (b-a)/n
    s = (f(a) + f(b))/2
    for i in range(1, n):
        s += f(a + i*h)
    return h*s

def f(x):
    return pow(math.e, -x)

a = 0
b = 1000000
n = 1000000

result = trapezoidal_rule(f, a, b, n)
print(result)