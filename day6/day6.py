class Memory:
    def __init__(self):
        self.blocks = list()
        self.seen = dict()
        self.count = 0
        self.didSeeConfig = False

    def getLargest(self):
        largest = max(self.blocks)
        index = self.blocks.index(largest)
        return [index, largest]

    def updateConfig(self):
        index_largest, largest = self.getLargest()
        self.blocks[index_largest] = 0
        for i in xrange(len(self.blocks)):
            self.blocks[i] += largest/len(self.blocks)
        for j in xrange(1, largest%len(self.blocks)+1):
            index = (index_largest+j)%len(self.blocks)
            self.blocks[index] += 1
        self.count += 1

    def checkIfSeen(self):
        cur_config = tuple(self.blocks)
        if cur_config in self.seen.keys():
            self.didSeeConfig = True
        else:
            self.seen[cur_config] = self.count
            self.didSeeConfig = False
    
    def getCurCount(self):
        return self.seen[tuple(self.blocks)]

mem = Memory()
with open("day6.txt", "r") as input:
    for line in input:
        for b in line.split():
            mem.blocks.append(int(b))
mem.seen[tuple(mem.blocks)] = 0
while not mem.didSeeConfig:
    mem.updateConfig()
    mem.checkIfSeen()

print mem.count - mem.getCurCount()   
