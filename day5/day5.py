def partOne():
    instruct = list()
    with open("day5.txt", "r") as input:
        for line in input:
            instruct.append(int(line))
    index = 0
    count = 0
    while index >= 0 and index < len(instruct):
        instruct[index] += 1
        index  = index + instruct[index] - 1
        count += 1
    print count

def partTwo():
    instruct = list()
    with open("day5.txt", "r") as input:
        for line in input:
            instruct.append(int(line))
    index = 0
    count = 0
    while index >= 0 and index < len(instruct):
        if instruct[index] >= 3:
            incr = -1
        else:
            incr = 1
        instruct[index] += incr
        index = index + instruct[index] - incr
        count += 1
    print count

partTwo()
