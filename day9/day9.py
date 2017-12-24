stack = []
groupMode = True
val = 1
score = 0
prev = 0
num_garbage = 0
with open("day9.txt","r") as input:
    for line in input:
        for i in xrange(len(line)):
            #print stack, score, val
            if groupMode:
                if line[i] == "<":
                    groupMode = False
                elif line[i] == "{":
                    if len(stack) > 0 and stack[-1] == "{":
                        val += 1
                    score += val
                    stack.append("{")
                elif line[i] == ",":
                    if line[i+1] != "<" and line[i-1] != ">":
                        stack.append(",")
                elif line[i] == "}":
                    if stack[-1] == "}":
                        val -= 1
                    stack.append("}")
            else:
                if stack[-1] == "!":
                    stack.pop()
                elif line[i] == "!":
                    stack.append("!")

                elif line[i] == ">":
                    groupMode = True
                else:
                    num_garbage += 1
print score
print num_garbage
