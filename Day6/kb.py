import re

class KB:
    def __init__(self):
        self.rules = []
        self.facts = {}
        self.dict = {}

    def load(self, code):
        lines = re.split(r'[\.]+ ?', code)
        # lines = code.split(/[\.]+ ?/);
        print(lines)
        for line in lines:
            if len(line.strip()) > 0:
                self.addRule(line)

    def isFact(self, term):
        if len(term) == 0:
            return True
        return self.facts.get(term) != None

    def check(self, rule):
        for term in rule['terms']:
            if self.isFact(term.strip()):
                continue
            else:
                return False
        return True

    def addFact(self, term):
        self.facts[term] = True
        print("addFact({})".format(term))

    def addRule(self, line):
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
        self.dict[head] = {
          'headHits': [rule],
          'bodyHits': []
        }

    def forwardChaining(self):
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
