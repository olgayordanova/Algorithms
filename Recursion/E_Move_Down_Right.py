def get_paths(row, col, matrix):

    if row>=len(matrix) or col >=len(matrix[0]):
        return 0

    if row==len(matrix)-1 and col == len(matrix[0])-1:
        return 1

    result = 0
    result+=get_paths(row+1, col, matrix)
    result+=get_paths(row, col+1, matrix)

    return result

n = int(input())
m = int(input())
matrix= [['-' for j in range (m)] for i in range (n)]

print(get_paths(0,0, matrix))