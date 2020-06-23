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
