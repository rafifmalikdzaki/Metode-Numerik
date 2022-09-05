def dev(f, x, h=0.000000001):
    return int((f(x+h) - f(x)) / h)

def f(x):
    return x ** 2 + x # x^2 + x 

print(dev(f, 5))