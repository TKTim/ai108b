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
