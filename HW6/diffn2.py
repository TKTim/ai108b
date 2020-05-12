
from math import *
#Truncation Errors = te

te = 2
step = 0.01
def df(f, x, h=step):
    return (f(x+te*h)-f(x-te*h))/(2*te*h)

def dfn(f, x, n, h=step):
    if (n == 0): return f(x)
    if (n == 1): return df(f,x,h)
    return (dfn(f, x+te*h, n-1) - dfn(f, x-te*h, n-1))/(2*te*h)

print('df(sin, pi/4)=', df(sin, pi/4))

for i in range(10):
    print('dfn(sin,', i, 'pi/4)=', dfn(sin, pi/4, i))