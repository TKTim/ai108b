欄位 | 內容
-----|--------
教學網站 | [邏輯推論](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96/A-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96%E7%B0%A1%E4%BB%8B)

範例檔案:kb,py
=

```
import re

class KB:
    def __init__(self): #物件的建構函數
        self.rules = [] #所有規則
        self.facts = {} #所有事實
        # self.dict = {}  #被滿足的事實，目前沒用到。

    def load(self, code): # 載入知識庫
        lines = re.split(r'[\.]+ ?', code)
        # lines = code.split(/[\.]+ ?/);
        print(lines)
        for line in lines:
            if len(line.strip()) > 0:
                self.addRule(line)

    def isFact(self, term):  # 判斷 term 是否為事實
        if len(term) == 0:
            return True
        return self.facts.get(term) != None

    # check 函數的作用
    #     以 鳥類 <= 會飛 & 生蛋. 為例
    #     rule['terms'] = ['會飛' , '生蛋']
    #     只要 ['會飛' , '生蛋'] 都被滿足了， check 就會傳回 true
    #     此時 forwardChaining 就會把結論 鳥類 加入事實庫。


    def check(self, rule): # 檢查規則 rule 是否所有前提都被滿足
        for term in rule['terms']:
            if self.isFact(term.strip()):
                continue
            else:
                return False
        return True

    def addFact(self, term):   # 把 term 加入事實庫
        self.facts[term] = True
        print("addFact({})".format(term))

    def addRule(self, line):     # 剖析規則
        m = re.match(r"^([^<=]*)(<=(.*))?$", line)
        head = "" if m.group(1)==None else m.group(1).strip()
        # print('addRule: m.group(3)=', m.group(3))
        terms= "" if m.group(3)==None else m.group(3).strip().split(r"&")
        print("rule:head={} terms={}".format(head, terms))
        rule = {
          'head': head,
          'terms':terms,
          'satisfy':False
        }
        self.rules.append(rule)
        '''
        self.dict[head] = {
          'headHits': [rule],
          'bodyHits': []
        }
        '''

    def forwardChaining(self):  # 前向推論的演算法
        while True:
            anySatisfy = False 

            for rule in self.rules:     # 對於每一條規則
                if not rule['satisfy']: # 如果該規則沒有被滿足
                    if self.check(rule):#就檢查該規則前提是否被滿足
                        self.addFact(rule['head']) # 如果是的話，就將結論加入事實庫
                        rule['satisfy'] = True # 設定規則以滿足
                        anySatisfy = True # 這次推論至少有一條新規則被滿足。
                
            if not anySatisfy:  #若沒有規則被滿足，推理就結束。
                break

        print("facts=", self.facts.keys())
```

實作: 冒險者文章 產生器
=

程式碼:
[generator.py](https://github.com/TKTim/ai108b/blob/master/HW5/generator.py)

結果:
=
```
獲勝結局
python .\generator.py 030 冒險開始了，在森林冒險名為030的笨蛋，因為 一隻 傷心的Siri 攻擊了030，導致030更加充滿鬥志。冒險已累積685賞金 按下Enter繼續冒險

冒險開始了，在城鎮冒險名為030的男人，有一天 一隻 傷心的領主 砍了030，所以030更加想回家睡覺。冒險已累積1355賞金 存夠了錢，所以去買了寶劍 按下Enter繼續冒險

冒險開始了，在城鎮冒險名為030的勇者，因為 一隻 白村民 攻擊了030，導致030更加想回家睡覺。冒險已累積1355賞金 按下Enter繼續冒險

冒險開始了，在城鎮冒險名為030的女人，因為 一群 傷心的魔王 砍了030，導致030更加想回家睡覺，但因為買了寶劍，所以打敗了魔王，冒險獲勝

死亡結局
冒險開始了，在城鎮冒險名為030的笨蛋，有一天 一位 白魔王 攻擊了030，所以030更加沮喪，但是傷勢過重，死掉了，冒險結束

平民結局
冒險開始了，在城鎮冒險名為030的男人，有一天 一位 生氣的Siri 砍了030，導致030更加沮喪。冒險已累積601賞金 按下Enter繼續冒險

冒險開始了，在城鎮冒險名為030的男人，因為 一位 黑穿越者 砍了030，所以030更加想回家睡覺。冒險已累積1173賞金 按下Enter繼續冒險

冒險開始了，在森林冒險名為030的勇者，有一天 一群 白哥布林 砍了030，導致030更加沮喪。冒險已累積1680賞金 存夠了錢，所以去買了寶劍 按下Enter繼續冒險

冒險開始了，在城鎮冒險名為030的勇者，有一天 一隻 生氣的穿越者 嘲笑了030，所以030更加沮喪。冒險已累積1680賞金 按下Enter繼續冒險

冒險開始了，在森林冒險名為030的女人，因為 一位 白領主 嘲笑了030，所以030更加想回家睡覺。冒險已累積1680賞金 因為一直沒遇到魔王，你決定將勇者的工作交給別人
```
