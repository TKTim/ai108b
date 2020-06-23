最大期望算法（Expectation-maximization algorithm)
=
[最大期望算法Wiki](https://zh.wikipedia.org/zh-tw/%E6%9C%80%E5%A4%A7%E6%9C%9F%E6%9C%9B%E7%AE%97%E6%B3%95?fbclid=IwAR3suFKizlBT-W79sVtsCPi_mDdoGMVsH3IjmIWUhekFF-7o4f_SwO7-UWw)
```
第一步是計算期望（E），利用對隱藏變量的現有估計值，計算其最大似然估計值；第二步是最大化（M），最大化在E步上求得的最大似然值來計算參數的值。M步上找到的參數估計值被用於下一個E步計算中，這個過程不斷交替進行。
```

估計無法觀測的數據 p()
=
```
   讓p,代表矢量 :定義的參數的全部數據的機率密度函數（連續情況下）或者機率質量函數（離散情況下），那麼從這個函數就可以得到全部數據的最大似然值，另外，在給定的觀察到的數據條件下未知數據的條件分布可以表示為：
```

numpy.exp
=
[exp](https://www.cnblogs.com/chengxin1982/p/7623583.html)
```
exp，高等數學里以自然常數e為底的指數函數
Exp：返回e的n次方，e是一個常數為2.71828 
Exp 函數 返回 e（自然對數的底）的冪次方。
```

numpy.dot
=
```
如果處理的是一維數組，則得到的是兩數組的內積。
```

numpy.計算
=
```
print '兩個數組相加：'
print np.add(a,b)
print '\n'
print '兩個數組相減：'
print np.subtract(a,b)
print '\n'
print '兩個數組相乘：'
print np.multiply(a,b)
print '\n'
print '兩個數組相除：'
print np.divide(a,b)
```


numpy.max
=
```
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
np.max(b, axis=0) #看結果是取出最大的一行
array([ 8, 9, 10, 11])
>>> np.max(b, axis=1) #看結果是取出最大的一列
array([ 3, 7, 11])
```


[老師範例](https://gitlab.com/ccckmit/ai2/-/blob/master/python/10-machineLearning/em/em.md?fbclid=IwAR1DEntZErjXGALE9eeKIuIFSWfZ1AfAomx7pjnN1RoZlZclQC0LyjsXdC4)

em.py
-

```
import numpy as np
import math
# 參考文獻：Numerical example to understand Expectation-Maximization -- http://ai.stanford.edu/~chuongdo/papers/em_tutorial.pdf
# What is the expectation maximization algorithm? (PDF) -- http://stats.stackexchange.com/questions/72774/numerical-example-to-understand-expectation-maximization

'''
計算 P(e|p)

ex: logP(e1|pA) = logP([5,5]|[0.6,0.4]) 
               = log(0.6^5*0.4^5) 
               = 5 log(0.6) + 5 log(0.4)

最後 P(e1|pA) = exp(logP(e1|pA)) = 0.6^5 + 0.4^5
'''
def P(e, p):
    logP = np.dot(e, np.log(p))
    return np.exp(logP)

'''
1st:  Coin B, {HTTTHHTHTH}, 5H,5T
2nd:  Coin A, {HHHHTHHHHH}, 9H,1T
3rd:  Coin A, {HTHHHHHTHH}, 8H,2T
4th:  Coin B, {HTHTTTHHTT}, 4H,6T
5th:  Coin A, {THHHTHHHTH}, 7H,3T
假如已經知道，1st, 4th 是 B, 2nd, 3rd, 5th 是 A, 
那就可以計算出 pA(heads) = 0.80 and pB(heads)=0.45
'''
def EM():
    e = [ [5,5], [9,1], [8,2], [4,6], [7,3] ]
    pA = [0.6, 0.4] #新增加:  初始值 正:0 反:1
    pB = [0.5, 0.5] #新增加:  初始值 正:0 反:1
    delta = 9.9999  #新增加:  疊帶差異值 停止值
    for _ in range(1000):
        print("pA={} pB={} delta={}".format(pA, pB, delta))
        sumA=[0,0]
        sumB=[0,0]
        for ei in e:
            # estimate
            a = P(ei, pA) # 用 A 去擲會產生 ei 的機率之 log
            b = P(ei, pB)
            wA = a/(a+b)   # = a 的權重
            wB = b/(a+b)   # = b 的權重
            eA = np.multiply(wA, ei) # A 的估計值
            eB = np.multiply(wB, ei) # B 的估計值
            # estimation 完成估計
            # maximization （先加總）
            sumA = np.add(sumA, eA)
            sumB = np.add(sumB, eB)

        npA = np.multiply(sumA, 1.0/np.sum(sumA)) # 新一版的 pA
        npB = np.multiply(sumB, 1.0/np.sum(sumB)) # 新一版的 pB
        # 計算差異，看看是否該停止了
        dA  = np.subtract(npA, pA)
        dB  = np.subtract(npB, pB)
        delta = np.max([dA, dB])
        if delta < 0.001: break #新增加:   是否該停止了
        # 更新 pA, pB 為新一版 
        pA = npA
        pB = npB

EM()

```
em.py 運作結果
-

![image](https://github.com/TKTim/ai108b/blob/master/09%20%E6%9C%80%E5%A4%A7%E6%9C%9F%E6%9C%9B%E7%AE%97%E6%B3%95%20%E3%80%81%20%E6%AD%B8%E7%B4%8D%E4%BA%86%E8%A8%B1%E5%A4%9A%E4%B9%8B%E5%89%8D%E4%B9%9F%E4%BD%BF%E7%94%A8%E5%88%B0%E7%9A%84%E5%87%BD%E7%A4%BA/1.png)

em.py 解析
=

整個程式的主旨便是照以下ex做的。
```
計算 P(e|p)

ex: logP(e1|pA) = logP([5,5]|[0.6,0.4]) 
               = log(0.6^5*0.4^5) 
               = 5 log(0.6) + 5 log(0.4)

最後 P(e1|pA) = exp(logP(e1|pA)) = 0.6^5 + 0.4^5
```

也就是

![im](https://github.com/TKTim/ai108b/blob/master/09%20%E6%9C%80%E5%A4%A7%E6%9C%9F%E6%9C%9B%E7%AE%97%E6%B3%95%20%E3%80%81%20%E6%AD%B8%E7%B4%8D%E4%BA%86%E8%A8%B1%E5%A4%9A%E4%B9%8B%E5%89%8D%E4%B9%9F%E4%BD%BF%E7%94%A8%E5%88%B0%E7%9A%84%E5%87%BD%E7%A4%BA/2.png)









