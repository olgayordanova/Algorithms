def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()

def can_place(row, col, rows, cols, right_diagonals, left_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonals:
        return False
    if (row + col) in right_diagonals:
        return False
    return True


def set_queen(row,col,matrix, rows, cols, right_diagonals, left_diagonals):
    matrix[row][col] = "*"
    rows.add(row)
    cols.add(col)
    right_diagonals.add(row+col)
    left_diagonals.add(row - col)


def delete_queen(row,col,matrix, rows, cols, right_diagonals, left_diagonals):
    matrix[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    right_diagonals.remove(row + col)
    left_diagonals.remove(row - col)

def put_queens(row, matrix, rows, cols, right_diagonals, left_diagonals):
    if row == 8:
        print_matrix(matrix)
        return
    for col in range(8):
        if can_place(row, col, rows, cols, right_diagonals, left_diagonals):
            set_queen(row,col,matrix, rows, cols, right_diagonals, left_diagonals)
            put_queens(row+1, matrix, rows, cols, right_diagonals, left_diagonals)
            delete_queen(row,col,matrix, rows, cols, right_diagonals, left_diagonals)


n=8
matrix= [["-" for j in range (8)] for i in range (8)]

put_queens(0, matrix, set(), set(), set(), set())



