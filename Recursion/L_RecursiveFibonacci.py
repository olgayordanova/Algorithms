n = int(input())

def fibonacci_el(n):
    if n<1:
        return 1
    return fibonacci_el(n-1)+fibonacci_el(n-2)

print(fibonacci_el (n-1))
# n = int(input())
# def fibonacci_el(n):
#     fib = []
#     fib.append(1)
#     fib.append(1)
#     for i in range (2, n+1):
#         fib.append(fib[i-1]+fib[i-2])
#     # print(fib)
#     return fib[-1]
#
# print(fibonacci_el (n))