# import numpy as np
# matrix = np.zeros((int(n),int(n)))
# matrix= [[0 for j in range (n)] for i in range (n)]

n = int(input())
vector = [0 for j in range(n)]

def generate_vector(inx, vector):
    if inx == len(vector):
        print("".join([str(el) for el in vector]))
        return
    for i in range(2):
        vector[inx] = i
        generate_vector(inx + 1, vector)

generate_vector(0, vector)


# def generate_vector(inx, n, vector):
#     if inx == n:
#         print("".join([str(el) for el in vector]))
#         return
#     for j in range(n):
#         for i in range(2):
#             vector[inx] = i
#             generate_vector(inx + 1, n, vector)
#         return vector
#
# generate_vector(0, n, vector)