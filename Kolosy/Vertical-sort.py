def matrix_print(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    print(" ")


n, m = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
    
solution_matrix = [[0 for _ in range(n)] for _ in range(m)]

for j in range(n):
    column = []
    for i in range(m):
        column.append(matrix[i][j])
    column.sort()
    for i in range(m):
        solution_matrix[i][j] = column[i]


matrix_print(solution_matrix, len(solution_matrix), len(solution_matrix[0]))



