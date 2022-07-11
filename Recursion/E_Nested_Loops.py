n = int(input())
vector = [1 for j in range(n)]

def generate_vector(inx, vector):
    if inx == len(vector):
        print(" ".join([str(el) for el in vector]))
        return
    for i in range(1, n+1):
        vector[inx] = i
        generate_vector(inx + 1, vector)

generate_vector(0, vector)