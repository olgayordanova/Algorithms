def get_areas(row, col, matrix):
    if row<0 or col<0 or row>=len(matrix) or col >=len(matrix[0]):
        return 0

    if matrix[row][col] !="-":
        return 0

    size = 1
    matrix[row][col] = "v"

    size+=get_areas(row-1, col, matrix)
    size+=get_areas(row+1, col, matrix)
    size+=get_areas(row, col-1, matrix)
    size+=get_areas(row, col+1, matrix)
    return size


rows = int(input())
cols = int(input())
matrix= [list(input()) for i in range (rows)]

counter = 0
lenths = []
for row in range(rows):
    for col in range(cols):
        size = get_areas(row, col, matrix)
        if size!=0:
            counter+=1
            lenths.append((size, row, col))

sorted_lenghs = sorted(lenths, key=lambda x:x[0], reverse=True)
print(f"Total areas found: {len(sorted_lenghs)}")
for i in range(1, len(sorted_lenghs)+1):
    print(f"Area #{i} at ({sorted_lenghs[i-1][1]}, {sorted_lenghs[i-1][2]}), size: {sorted_lenghs[i-1][0]}")
