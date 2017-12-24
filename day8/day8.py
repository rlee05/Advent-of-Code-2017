def satisfiesCondition(val, op, op_val):
    if op == ">" and val > op_val:
        return True
    elif op == "<" and val < op_val:
        return True
    elif op == "<=" and val <= op_val:
        return True
    elif op == ">=" and val >= op_val:
        return True
    elif op == "==" and val == op_val:
        return True
    elif op == "!=" and val != op_val:
        return True
    return False

def getIncrVal(incr, val):
    if incr == "inc":
        return val
    else:
        return val*-1

def partOne():
    reg_dict = dict()
    with open("day8.txt", "r") as input:
        for line in input:
            reg_a, sign, val, cond, reg_b, op, op_val = line.split()
            if reg_a not in reg_dict:
                reg_dict[reg_a] = 0

            if reg_b not in reg_dict:
                reg_dict[reg_b] = 0

            if satisfiesCondition(reg_dict[reg_b], op, int(op_val)):
                incr_val = getIncrVal(sign, int(val))
                reg_dict[reg_a] += incr_val
    return max(reg_dict.itervalues())

def partTwo():
    reg_dict = dict()
    largest = 0
    with open("day8.txt", "r") as input:
        for line in input:
            reg_a, sign, val, cond, reg_b, op, op_val = line.split()
            if reg_a not in reg_dict:
                reg_dict[reg_a] = 0

            if reg_b not in reg_dict:
                reg_dict[reg_b] = 0

            if satisfiesCondition(reg_dict[reg_b], op, int(op_val)):
                incr_val = getIncrVal(sign, int(val))
                reg_dict[reg_a] += incr_val
                largest = max(largest, reg_dict[reg_a])
    return largest


#print partOne()
print partTwo()
            