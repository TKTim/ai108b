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
