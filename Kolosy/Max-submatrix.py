#import numpy as np


n,k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def get_submatrix(matrix, n, k):
    submatrices = []
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            submatrix = [row[j:j + k] for row in matrix[i:i + k]]
            submatrices.append(submatrix)
    return submatrices

submatrices = get_submatrix(matrix,n,k)

def fmax(matrix):
    solution = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cross_product = sum(matrix[i][k] * matrix[k][j] for k in range(len(matrix[0])))
            solution += cross_product
    
    return solution


max = 0
for x in submatrices:
    if fmax(x) > max:
        max = fmax(x)

print(max)



