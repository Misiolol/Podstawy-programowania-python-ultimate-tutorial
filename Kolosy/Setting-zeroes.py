n,m = map(int, input().split())

matrix = []
output_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
output_matrix = [row[:] for row in matrix]

def matrix_print(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    print(" ")
    
    
def setting(arr, i, j):
    for _ in range(n):
        arr[_][j] = 0
        #matrix_print(arr, n, m)
    for _ in range(m):
        arr[i][_] = 0
        #matrix_print(arr, n, m)
        
        
#? iterating thorough matrix
def setting_zeroes(matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                #! 0 found
                setting(output_matrix, i, j)
                #print("zamieniam")
    
setting_zeroes(matrix)
matrix_print(output_matrix, n, m)