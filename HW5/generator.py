import os, re,sys
import random as r

'''
S => NP VP 句子 = 名詞子句 接 動詞子句
NP => Det Adj* N PP* 名詞子句 = 定詞 接 名詞
VP => V NP 動詞子句 = 動詞 接 名詞子句 接副詞子句
'''

def S():
    return  r.choice(before) + ' ' + NP() + ' ' + VP()

def S2():
    return  r.choice(after) + Name2 + STATE()

def Start():
    return STORYBOARD() + '名為' + Name2 + LABEL()

#argv轉字串
def ch(start):
    a = start.replace("[","")
    b = a.replace("]","")
    c = b.replace("'","")
    return c

adj = ['白', '黑', '傷心的', '生氣的']
before = ['因為', '有一天']
after = ['所以' , '導致']
storyboard = ['冒險開始了，在城鎮冒險', '冒險開始了，在森林冒險']

Name = sys.argv[1:]
str4 = "".join(Name)
Name2 = ch(str4)
state = ['更加沮喪', '更加充滿鬥志', '更加想回家睡覺']
Label = ['的女人，', '的男人，' ,'的笨蛋，', '的勇者，']

def STATE():
    return r.choice(state)

def NP():
    return DET() + ' ' + ADJ() + '' + N() 

def VP():
    return V() + Name2

def ADJ():
    return r.choice(adj)

def N():
    return r.choice(['哥布林', '巨魔','冒險者','魔王','村民','領主','Siri','穿越者'])

def V():
    return r.choice(['攻擊了', '嘲笑了', '砍了'])

def DET():
    return r.choice(['一群', '一隻', '一位'])

def LABEL():
    return r.choice(Label)

def STORYBOARD():
    return r.choice(storyboard)
def Money():
    return r.randint(500,700)
money = 0
a =0
for i in range(5):
    story = Start() +  S() + '，' + S2()
    if a==1:
        money= money
    elif a==0:
        money = money + Money()
    if '魔王' in story and a ==0:
        print (story + '，但是傷勢過重，死掉了，冒險結束')
        break
    elif '魔王' in story and a ==1:
        print (story + '，但因為買了寶劍，所以打敗了魔王，冒險獲勝')
        break
    else:
        print (story + '。冒險已累積' + str(money) + '賞金')
    if money >= 1200 and a==0:
        print('存夠了錢，所以去買了寶劍')
        a =1 
    if i==4:
        print('因為一直沒遇到魔王，你決定將勇者的工作交給別人')
    if i!=4:
        call = input('按下Enter繼續冒險'); 
    print('---------------------------')

        
