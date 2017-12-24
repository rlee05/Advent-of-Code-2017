from collections import Counter
from collections import deque

class Disc:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.weight = None

def setup():
    disc_dict = dict()
    with open("day7.txt") as input:
        for line in input:
            data = line.split()
            parent_name = data[0]
            if parent_name not in disc_dict:
                disc_dict[parent_name] = Disc(parent_name)
            disc_dict[parent_name].weight = int(data[1].strip("() "))
            if len(data) > 3:
                for i in xrange(3, len(data)):
                    disc_name = data[i].strip(", ")
                    if disc_name not in disc_dict:
                        disc_dict[disc_name] = Disc(disc_name)
                    disc_dict[disc_name].parent = parent_name
                    disc_dict[parent_name].children.append(disc_name)

    return disc_dict

def partOne(disc_dict):
    # Assume all discs are part of one tree so start at a any disc
    cur = disc_dict.itervalues().next()
    while cur.parent != None:
        cur = disc_dict[cur.parent]
    return cur.name   

def makeStack(disc_dict, disc_name):
    stack = []
    queue = deque()
    queue.append([disc_name])
    while len(queue) > 0:
        layer = queue.popleft()
        stack.append(layer)
        for disc in layer:
            children = disc_dict[disc].children
            if len(children) > 0:
                queue.append(children)

    return stack    

def getWeight(disc_dict, disc):
    children = disc_dict[disc].children
    weight = disc_dict[disc].weight
    if len(children) > 0:
        for child in children:
            weight += getWeight(disc_dict, child)
    return weight
    
def partTwo(disc_dict, stack):
    while len(stack) > 0:
        layer = stack.pop()
        weights = []
        for disc in layer:
            weights.append(getWeight(disc_dict, disc))
        counter = Counter(weights)
        common_counter = counter.most_common()

        if len(common_counter) > 1:
            least_common = common_counter[-1][0]
            most_common = common_counter[0][0]
            index = weights.index(least_common)
            bad_disc = disc_dict[layer[index]]
            return bad_disc.weight + most_common - least_common  

disc_dict = setup()
disc_name = partOne(disc_dict)
stack = makeStack(disc_dict, disc_name)
result = partTwo(disc_dict, stack)
print result