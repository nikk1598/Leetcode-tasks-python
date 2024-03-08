import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.lst.append(val)
            self.d[val] = len(self.lst)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            index = self.d[val]
            self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
            self.d[self.lst[index]] = index
            self.lst.pop()
            del self.d[val]
            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()