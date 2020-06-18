爬山演算法
=
Since we only reviewed Python on Day1, so I didn't have many things to write here.

hillClimbing1.py
-
```
#簡易爬山演算法
def hillClimbing(f, x, dx=0.01):
    while (True):

        print(' x={:.3f} f(x)={:.3f}'.format(x, f(x)))
        if f(x+dx)>f(x): #如果右f(x-dx) >目前高度 則向右走
            x = x + dx
        elif f(x-dx)>f(x): #如果左f(x-dx) >目前高度 則向左走
            x = x - dx
        else: #如果左右都不比現在高 那這裡變為頂點(山頂)
            break
    return x

#高度函數
def f(x):
    return -1*(x*x+3*x+5)  #此圖山頂在y軸左側 可見一開始x是慢慢減少的
    # return -1*abs(x*x-4)

hillClimbing(f, 0)
```

hillClimbing2.py
-
```
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
```

hillClimbing2r.py
-
```
import random  #隨機爬山演算法
# 整體架構，使用亂數向自己的鄰居比大小，若自己比


def hillClimbing(f, x, y, h=0.01):
    failCount = 0   #連續測試的失敗次數
    while (failCount < 10000):
        fxy = f(x, y)
        dx = random.uniform(-h, h+0.01)  #random.uniform 是取隨機變數 -h ~~h之間(不含h)
        dy = random.uniform(-h, h+0.01)  
        #我嘗試增加h的大小 看是否會有計算錯誤 但只要數值不大 都沒問題 +0.05不行
        if f(x+dx, y+dy) >= fxy:
            x = x + dx
            y = y + dy
            print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
        else:
            failCount = failCount + 1
    return (x,y,fxy)

def f(x, y):
    return -1 * ( x*x -2*x + y*y +2*y - 8 )

hillClimbing(f, 0, 0)
```
