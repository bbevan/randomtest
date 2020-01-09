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
        # Q? Why is this out in the open, and not in main?
        self.rnglist = []
        self.rnglist = self.createRngList()

    def randomtest_True(self, method = lambda x:x, *expected):
        # it's more complicated than this.
        # gotta-be.
        results = []
        #non_results = []
        i = len(expected)
        for x in range(i):
            if (method == expected[x]):
                results.append(expected[x])
            #else:
                #non_results = expected[x].append()
        return results == expected


