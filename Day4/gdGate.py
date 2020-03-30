import numpy as np
import math
import gd3 as gd

def sig(t):
    return 1.0/(1.0+math.exp(-t))

o = [0,0,0,1] # and gate outputs
# o = [0,1,1,1] # or gate outputs
# o = [0,1,1,0] # xor gate outputs
def loss(p):
    [w1,w2,b] = p
    #AND Gate 經過sigmoid()函數轉換
    o0 = sig(w1*0+w2*0+b)  #0,0
    o1 = sig(w1*0+w2*1+b)  #0,1
    o2 = sig(w1*1+w2*0+b)  #1,0
    o3 = sig(w1*1+w2*1+b)  #1,1
    delta = np.array([o0-o[0], o1-o[1], o2-o[2], o3-o[3]]) #輸出-標準答案
    #差距越小越好
    print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    print('np.linalg.norm = {}'.format(np.linalg.norm(delta, 2)) )
    return np.linalg.norm(delta, 2) #取平方加總 
    #回歸法


p = [0.0, 0.0, 0.0] # [w1,w2,b] 

#最後以回歸法算出的loss作為gd2.gradientDescendent的f函數，對p做偏微分
gd.gradientDescendent(loss, p, max_loops=1500)
