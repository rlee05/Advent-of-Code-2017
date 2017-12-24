def gotCaught(layer, range, start_time):
    if layer+start_time == 0:
        return True
    elif range == 1:
        return True
    num_steps = (range-1)*2
    if (layer+start_time)%num_steps == 0:
        return True
    return False

firewall = dict()
caught_flag = False
delay = 0

with open('day13.txt','r') as input:
    for line in input:
        layer, range = line.split(': ')
        firewall[int(layer)] = int(range)
        result = gotCaught(int(layer), int(range), delay)
        if result and not caught_flag:
            caught_flag = True
        
while(caught_flag):
    delay += 1
    caught_flag = False
    for layer in firewall.keys():
        caught_flag = gotCaught(layer, firewall[layer], delay)
        if caught_flag:
            break
print(delay)