import random

class RandomTest:

    def __init__(self, *seed):
        if seed:
            self.seed = seed
            random.seed(self.seed)
        else:
            self.seed = ""
        self.rnglist = []

    def createRngList(self):
        for i in range(10):
            self.rnglist.append(random.randint(0,1))

    
myObj = RandomTest(12345678)
myObj.createRngList()
print(myObj.rnglist)