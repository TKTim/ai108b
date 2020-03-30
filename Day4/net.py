class Node:
    def __init__(self, v = 0, g = 0):
        self.v = v # 輸出值 (f(x))
        self.g = g # 梯度值 (偏微分)

    def __str__(self):
        return 'v:{self.v} g:{self.g}'.format(self=self) #轉成格式化字串

class Gate:
    def __init__(self, o, x, y, f, gfx, gfy):  #輸出 = o,x和y為輸入,對X取偏微分 = gfx
        self.o = o
        self.x = x
        self.y = y
        self.f = f
        self.gfx = gfx
        self.gfy = gfy

    def forward(self):
        self.o.v = self.f(self.x.v, self.y.v)
        #使用輸出的 輸出值 (f(x)) = 呼叫f
        return self.o.v

    def backward(self):
        x, y, o, gfx, gfy = self.x, self.y, self.o, self.gfx, self.gfy
        #反向公式
        x.g += gfx(x.v,y.v) * o.g
        y.g += gfy(x.v,y.v) * o.g

    def adjust(self, step=0.001): # 朝逆梯度的方向走一小步 step
        x, y = self.x, self.y
        x.v -= step*x.g
        y.v -= step*y.g
        x.g = 0
        y.g = 0

class Net:
    def __init__ (self):
        self.gates = []

    def variable (self, v, g=0):
        return Node(v, g)

    def op (self, x, y, f, gfx, gfy):  #創建新的閘
        o = Node()
        g = Gate(o, x, y, f, gfx, gfy)
        self.gates.append(g)
        self.o = o
        return o

    def add (self, x, y):
        return self.op(x, y, lambda x,y:x+y, lambda x,y:1, lambda x,y:1) 
        #x+y 對x 取偏微分便是1 對y 取偏微分便是1
    def mul (self, x, y):
        return self.op(x, y, lambda x,y:x*y, lambda x,y:y, lambda x,y:x) 
        #x*y  對x 取偏微分便是y 對y 取偏微分便是x

    def forward(self): # 正向傳遞計算結果 對每一個閘做
        for gate in self.gates:
            gate.forward() 
        return self.o.v

    def backward(self): # 反向傳遞計算梯度   對每一個閘做
        self.o.g = 1 # 設定輸出節點 o 的梯度為 1
        for gate in reversed(self.gates): # 反向傳遞計算每個節點 Node 的梯度 g
            gate.backward()

    def adjust(self, step=0.01): # 朝逆梯度的方向走一小步
        for gate in self.gates:
            gate.adjust(step)

    # 使用 forward-backward 的方式計算梯度的梯度下降法
    def gradient_descendent (self, maxLoops=100, dumpPeriod=1, step=0.01):
        for loop in range(maxLoops):
            energy = self.forward()  #從頭往下算 也就是正向算法便稱forward()
            if loop % dumpPeriod==0:
                print(loop, ' => ', energy)
            self.backward()
            self.adjust(step)

