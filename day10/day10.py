class CircularArray:
    def __init__(self, length):
        self.arr = range(length)
        self.length = length

    def swap(self, index1, index2):
        temp = self.arr[index1]
        self.arr[index1] = self.arr[index2]
        self.arr[index2] = temp

def partOne():
    cur_index = 0
    skip = 0
    circ_arr = CircularArray(256)

    with open("day10.txt","r") as input:
        for line in input:
            data = line.split(",")
            for num in data:
                length = int(num)
            # print circ_arr.arr, cur_index, length
                for i in xrange(length/2):
                    start_index = (cur_index+i)%circ_arr.length
                    end_index = (cur_index + length - 1 - i)%circ_arr.length
                    circ_arr.swap(start_index, end_index)
                #print circ_arr.arr
                cur_index = (cur_index + length + skip)%circ_arr.length
                skip += 1
    print circ_arr.arr[0]*circ_arr.arr[1]

def generateDenseHash(data):
    print len(data)
    dense_hash = []
    for h in xrange(16):
        xor_result = data[h*16]
        for a in xrange(1, 16):
            index = h*16+a
            xor_result = xor_result^data[index]
        dense_hash.append(xor_result)
    return dense_hash

def generateHex(dense_hash):
    hex_array = []
    for num in dense_hash:
        hex_str = hex(num)
        hex_array.append(hex_str[2:])
    return "".join(hex_array)

def partTwo():
    ascii_data = []
    with open("day10.txt","r") as input:
        for line in input:
            for char in line:
                ascii_data.append(ord(char))
        ascii_data = ascii_data + [17, 31, 73, 47, 23]
    cur_index = 0
    skip = 0
    circ_arr = CircularArray(256)
    for k in xrange(64):
        for num in ascii_data:
            length = int(num)
            # print circ_arr.arr, cur_index, length
            for i in xrange(length/2):
                start_index = (cur_index+i)%circ_arr.length
                end_index = (cur_index + length - 1 - i)%circ_arr.length
                circ_arr.swap(start_index, end_index)
            #print circ_arr.arr
            cur_index = (cur_index + length + skip)%circ_arr.length
            skip += 1

    dense_hash = generateDenseHash(circ_arr.arr)
    hex_str = generateHex(dense_hash)
    return hex_str
        
print partTwo()
