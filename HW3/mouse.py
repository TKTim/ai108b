
def matrixPrint(m) :
    #for i in range(m.length):
    i =0
    j = 0
    for i in range(6):
        for j in range(8):
            print(m[i][j],end='')
        print() 

def strset(s, i, c) :
    m[s][i] = c


def findPath(m, x, y) :
    print("=========================")
    print("x= {} y= {}".format(x,y))
    matrixPrint(m)
    if x>=6 or y>=8 :
        return
    if m[x][y] == '*' :
        return
    if m[x][y] == '+':
        return
    if m[x][y] == ' ' :
        strset(x, y, '.')
    if m[x][y] == '.' and (x == 5 or y==7) :  
        return
    if  y<7 and m[x][y+1]==' ' : #向右
        findPath(m, x,y+1)
            
    if  x<5 and m[x+1][y]==' ' : #向下
        findPath(m, x+1,y) 
            
    if y>0 and m[x][y-1]==' ' : #向左
        findPath(m, x,y-1)
            
    if x>0 and m[x-1][y]==' ' : #向上
        findPath(m, x-1,y)
            
    #m[x][y]='+'
    return x,y


m =[    ["*","*","*","*","*","*","*","*"], 
        ["*","*"," ","*"," ","*","*","*"],
        [" "," "," "," "," ","*","*","*"],
        ["*"," ","*","*","*","*","*","*"],
        ["*"," "," "," "," "," ","*","*"],
        ["*","*","*","*","*"," ","*","*"]
    ]
    
findPath(m, 2, 0)
print("=========================")
matrixPrint(m)
