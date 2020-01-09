import random

class RandomTest:

    def createRngList(self):
        if self.rnglist == []:    
            for i in range(10):
                self.rnglist.append(random.randint(0,1))
        
        return self.rnglist
    
    def __init__(self, *seed):
        if seed:
            self.seed = seed
        else:
            self.defaultseed = 123456789123456789
            self.seed = self.defaultseed
        
        random.seed(self.seed)

        # create the rnglist
        self.rnglist = []
        self.rnglist = self.createRngList()

        # on init, create the rnglist
        #self.createRngList()




myObj = RandomTest()
myObj.createRngList()
print(myObj.rnglist)
