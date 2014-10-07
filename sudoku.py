f = open( "test.txt" )
matrix = [[0 for i in range(9)] for i in range(9)]

for i, line in enumerate(f):
    for j, val in enumerate(line):
        if val == '\n': continue
        else: matrix[i][j] = int(val)
print(matrix)

def check( _matrix, x, y ):
    num = _matrix[x][y]
    for i in range(9):
        if _matrix[i][y] == num and i != x:
            return False
        if _matrix[x][i] == num and i != y:
            return False
    xx = int( x/3 )*3
    yy = int( y/3 )*3
    for i in range(3):
        for j in range(3):
            if xx+i == x and yy+j == y: 
                continue
            elif _matrix[xx+i][yy+j] == num:
                return False

    return True

def recursive( _matrix, x, y ):
    if x == 9 and y == 0:
        print( _matrix )
    if x >8 or y >8:
        return
    if _matrix[x][y] == 0:
        for i in range(1,10):
            _matrix[x][y] = i
            if check( _matrix, x, y ):
                next_y = y+1
                next_x = x+ int( next_y/9 )
                next_y = next_y % 9
                recursive( _matrix, next_x, next_y )
            _matrix[x][y] = 0
    else:
        next_y = y+1
        next_x = x+ int( next_y/9 )
        next_y = next_y % 9
        recursive( _matrix, next_x, next_y )
recursive( matrix, 0, 0 )       
