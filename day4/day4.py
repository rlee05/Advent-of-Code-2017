def partOne():    
    total = 0
    with open("day4.txt", "r") as input:
        for line in input:
            total += 1
            seen = set()
            word_array = line.split()
            for word in word_array:
                if word in seen:
                    total -= 1
                    break
                else:
                    seen.add(word)
    print total

def partTwo():
    total = 0
    with open("day4.txt","r") as input:
        for line in input:
            total += 1
            seen = set()
            word_array = line.split()
            for word in word_array:
                s = "".join(sorted(word))
                if s in seen:
                    total -= 1
                    break
                else:
                    seen.add(s)
    print total

partTwo()
