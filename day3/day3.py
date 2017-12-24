from enum import Enum
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def partOne():
    target = 277678
    i = 1
    while (i*i) < target:
        i += 2
    layer = (i-1)/2
    position = (target - (i-2)*(i-2))%(i-1)
    offset = abs(position - layer)
    print offset+layer

def expandGrid(grid):
    side_length = len(grid)+2
    for row in grid:
        row.insert(0, 0)
        row.append(0)
    grid.append([0 for i in xrange(side_length)])
    grid.insert(0, [0 for i in xrange(side_length)])
    return grid

def getSum(row, col, grid):
    sum = 0
    if row-1 >= 0:
        try:
            sum += grid[row-1][col]
        except:
            pass
        if col-1 >= 0:
            try:
                sum += grid[row-1][col-1]
            except:
                pass
        if col+1 < len(grid[row]):
            try:
                sum += grid[row-1][col+1]
            except:
                pass
    if row+1 < len(grid):
        try:
            sum += grid[row+1][col]
        except:
            pass
        if col-1 >= 0:
            try:
                sum += grid[row+1][col-1]
            except:
                pass
        if col+1 < len(grid[row]):
            try:
                sum += grid[row+1][col+1]
            except:
                pass
    if col-1 >= 0:
        try:
            sum += grid[row][col-1]
        except:
            pass
    if col+1 < len(grid[row]):
        try:
            sum += grid[row][col+1]
        except:
            pass
    return sum

def coordToIndex(x, y, side_length):
    row = side_length/2+y
    col = side_length/2+x

    return [row, col]

def partTwo(target):
    x = 0
    y = 0
    row = 0
    col = 0
    side_length = 1
    dir = Direction.RIGHT
    grid = [[1]]
    while grid[row][col] < target:
        #print dir, x, y
        if dir == Direction.RIGHT:
            if col == side_length-1:
                grid = expandGrid(grid)
                side_length += 2
                dir = Direction.UP
            x += 1
            
        elif dir == Direction.UP:
            if row == 1:
                dir = Direction.LEFT
            y -= 1
        elif dir == Direction.LEFT:
            if col == 1:
                dir = Direction.DOWN
            x -= 1
        elif dir == Direction.DOWN:
            print row
            if row == side_length-1:
                dir = Direction.RIGHT
            else:
                y += 1

        row, col = coordToIndex(x, y, side_length)
        grid[row][col] = getSum(row, col, grid)
        #print grid[row][col], row, col, side_length
    print grid[row][col]
partTwo(277678)
