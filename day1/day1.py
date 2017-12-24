sum = 0
with open("day1.txt","r") as input:
    for line in input:
        num_steps = len(line)/2
        for i in xrange(len(line)):
            cur = int(line[i])
            next = int(line[(i+num_steps)%len(line)])
            if cur == next:
                sum += cur
print sum
