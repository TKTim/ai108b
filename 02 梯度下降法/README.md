我的學習筆記(網站):
https://timleesdailyfactory.blogspot.com/2020/03/ai.html


會使用到numpy
https://zh.wikipedia.org/wiki/NumPy

gd1.py
-
```
import numpy as np
from numpy.linalg import norm

# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp

# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, step=0.01):
    p = p0.copy()
    i = 0
    while (True): ###使用while不斷向下
        i += 1
        fp = f(p)
        gp = grad(f, p) # 計算梯度 gp
        glen = norm(gp) # norm = 梯度的長度 (步伐大小) Import from numpy.linalg
        print('{:d}:p={:s} f(p)={:.3f} gp={:s} glen={:.5f}'.format(i, str(p), fp, str(gp), glen))
        if glen < 0.00001:  # 如果步伐已經很小了，那麼就停止吧！
            break
        gstep = np.multiply(gp, -1*step) # gstep = 逆梯度方向的一小步
        ###正梯度會向上 逆梯度才是向下
        p +=  gstep # 向 gstep 方向走一小步
    return p # 傳回最低點！
```

gdTest.py
-
```
import gd1 as gd

def f(p):
    [x,y] = p
    return x*x + y*y

p = [1.0, 3.0]
gd.gradientDescendent(f, p)
```


```
NumPy是Python語言的一個擴充程式庫。支援高階大量的維度陣列與矩陣運算，此外也針對陣列運算提供大量的數學函式函式庫。
NumPy的前身Numeric最早是由Jim Hugunin與其它協作者共同開發，
2005年，Travis Oliphant在Numeric中結合了另一個同性質的程式庫Numarray的特色，
並加入了其它擴充功能而開發了NumPy。NumPy為開放原始碼並且由許多協作者共同維護開發。
```

gd1.py 為梯度下降法
gdTest.py 會引用gd1.y 來做

梯度向下法
https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/03-%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF/B-%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95


證明Xor無法在單神經網路下執行
=

![image](https://github.com/TKTim/ai108b/blob/master/02%20%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95/%E8%A8%BB%E8%A7%A3%202020-03-19%20123929.png)
