matrix = [[0 for _ in range(9)] for __ in range(9)]

with open("test.txt") as f:
    for i, line in enumerate(f):
        for j, val in enumerate(line):
            if val == '\n' or val == ' ':
                continue
            else:
                matrix[i][j] = int(val)
print(matrix)


def check(_matrix, x, y):
    num = _matrix[x][y]
    for i in range(9):
        if _matrix[i][y] == num and i != x:
            return False
        if _matrix[x][i] == num and i != y:
            return False
    xx = int(x/3)*3
    yy = int(y/3)*3
    for i in range(3):
        for j in range(3):
            if xx+i == x and yy+j == y:
                continue
            elif _matrix[xx+i][yy+j] == num:
                return False

    return True


def recursive(_matrix, x, y):
    if x > 8:
        for _ in _matrix:
            print(_)
        return

    next_y = y+1
    next_x = x + int(next_y/9)
    next_y = next_y % 9

    if _matrix[x][y] == 0:
        for i in range(1, 10):
            _matrix[x][y] = i
            if check(_matrix, x, y):
                recursive(_matrix, next_x, next_y)
            _matrix[x][y] = 0
    else:
        recursive(_matrix, next_x, next_y)
recursive(matrix, 0, 0)
