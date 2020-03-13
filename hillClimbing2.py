import random

def hillClimbing(f, x, y, h=0.01): #此為立體圖形 因此有x,y兩個向量
    while (True):
        fxy = f(x, y)
        print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
        if f(x+h, y) >= fxy:    #比較一點的四個方位 上下左右
            x = x + h
        elif f(x-h, y) >= fxy:
            x = x - h
        elif f(x, y+h) >= fxy:
            y = y + h
        elif f(x, y-h) >= fxy:
            y = y - h
        else:
            break
    return (x,y,fxy)

def f(x, y):
    return -1 * ( x*x - 2*x + y*y + 2*y - 8 )

hillClimbing(f, 0, 0)