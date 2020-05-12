Result
=
PS F:\06 資工\06 大三下\AI\Myfile> python .\root2.py
root of 1x^2+4x+5= [0j, (-2+0j)]


Code
=
import math
import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    if (t < 0):
        raise Exception('沒有實根')
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]


print("root of 3x^2+6x+0=", root2(3,6,0))



程式編寫
=
在Python當中複數用「j」或是「J」來表示。

如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块：
[參考網站](https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p06_complex_math.html)
>>> import cmath
>>> cmath.sin(a)
(24.83130584894638-11.356612711218174j)
>>> cmath.cos(a)
(-11.36423470640106-24.814651485634187j)
>>> cmath.exp(a)
(-4.829809383269385-5.5920560936409816j)
>>>
