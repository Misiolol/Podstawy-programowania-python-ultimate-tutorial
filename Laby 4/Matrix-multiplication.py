def multiply_matrices(A, B):
    rows_in_matrix_A = len(A)
    columns_in_matrix_A = len(A[0])
    rows_in_matrix_B = len(B)
    columns_in_matrix_B = len(B[0])

    if columns_in_matrix_A != rows_in_matrix_B:
        print(-1)

    solution = [[0 for _ in range(columns_in_matrix_B)] for _ in range(rows_in_matrix_A)]

    for i in range(rows_in_matrix_A):
        for j in range(columns_in_matrix_B):
            for k in range(columns_in_matrix_A):
                solution[i][j] += A[i][k] * B[k][j]

    return solution



w1, h1 = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(h1)]

w2, h2 = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(h2)]

result = multiply_matrices(matrix1, matrix2)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=" ")
    print()
    
