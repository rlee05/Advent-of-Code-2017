def getInput(filename):
    input = open(filename,"r")
    data = input.readline().split(",")
    input.close()
    return data

data = getInput("day11-test.txt")
position = [0,0,0]
for dir in data:
    if dir == "nw":
        position[0] += 1
    elif dir == "se":
        position[0] -= 1
    elif dir == "n":
        position[1] += 1
    elif dir == "s":
        position[1] -= 1
    elif dir == "ne":
        position[2] +=1
    elif dir == "sw":
        position[2] -= 1

if (position[0] > 0 and position[2] > 0) or (position[0] < 0 and position[2] < 0):
    sign = abs(position[0])/position[0]
    delta = min(abs(position[0]), abs(position[2]))*sign
    position[1] += delta
    position[0] -= delta
    position[2] -= delta
    
print position
