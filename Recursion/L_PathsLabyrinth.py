# You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with 'e'.
# •	Empty cells are marked with a dash '-'.
# •	Walls are marked with a star '*'.

def get_paths(row, col, matrix, direction, path):

    if row<0 or col<0 or row>=len(matrix) or col >=len(matrix[0]):
        return

    if matrix[row][col] =="*":
        return

    if matrix[row][col] =="v":
        return

    path.append(direction)

    if matrix[row][col]  =="e":
        print("".join(path))
    else:
        matrix[row][col] = "v"

        get_paths(row-1, col, matrix, 'U', path)
        get_paths(row+1, col, matrix, 'D', path)
        get_paths(row, col-1, matrix, 'L', path)
        get_paths(row, col+1, matrix, 'R', path)
        matrix[row][col] = "-"

    path.pop()


n = int(input())
m = int(input())
matrix= [list(input()) for i in range (n)]


get_paths(0,0, matrix, '',[])
