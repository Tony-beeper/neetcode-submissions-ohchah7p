class RandomizedSet:

    def __init__(self):
        self.randomizedSet = {}
        self.lst = []
        

    def insert(self, val: int) -> bool:            
        if self.randomizedSet.get(val) != None:
            return False
        idx = len(self.lst)
        self.lst.append(val)
        self.randomizedSet[val] = idx
        return True
        

    def remove(self, val: int) -> bool:
        if self.randomizedSet.get(val) == None:
            # self.randomizedSet[val] = None
            return False
        last_val = self.lst[-1]
        idx = self.randomizedSet[val]
        self.lst[idx] = last_val
        self.randomizedSet[last_val] = idx
        self.randomizedSet.pop(val)
        self.lst.pop(-1)
        return True



    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()