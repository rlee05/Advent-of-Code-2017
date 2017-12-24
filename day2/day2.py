def partOne():
    sum = 0
    with open("day2.txt","r") as input:
        for line in input:
            line = line.split()
            int_array = map(int, line)
            sum += max(int_array)-min(int_array)
    print(sum)

def partTwo():
    sum = 0
    with open("day2.txt","r") as input:
        for line in input:
            line = line.split()
            int_array = sorted(map(int, line), reverse=True)
            total = len(int_array)
            for i in xrange(total):
                for j in xrange(i+1,total):
                    if int_array[i]%int_array[j] == 0:
                        sum += int_array[i]/int_array[j]

    print(sum)

partTwo()