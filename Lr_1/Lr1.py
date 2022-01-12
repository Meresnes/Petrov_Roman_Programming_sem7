# Написание программы для численного интегрирования площади под кривой.
import math

def integrate(a, b, n_iter=1000):

    n = n_iter
    s = float(0)
    h = ((b - a) / n)
    x = a + h
    while (x <= b):
        f = math.sin(x)**2
        s += 1 / f
        x += h
    result = float(h * s)
    print('Результат = {:.9}'.format(result ))
    return result
a = float(input('a:'))
b = float(input('b:'))
integrate(a,b)
if __name__ == '__main__':
    pass

