def getPenalty(layer, range):
    if layer == 0:
        return 0
    elif range == 1:
        return layer
    num_steps = (range-1)*2
    if layer%num_steps == 0:
        return layer*range
    else:
        return 0

input = open('day13_part1.txt','r')
sum = 0
line = input.readline()
while line != None:
    print line
    layer, range = line.split(': ')
    sum += getPenalty(int(layer), int(range))
    line = input.readline()
    print(sum)
print(sum)