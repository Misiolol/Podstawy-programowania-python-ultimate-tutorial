n,k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def get_submatrix(matrix, n, k):
    submatrix = []
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            submatrix = [row[j:j + k] for row in matrix[i:i + k]]
            submatrix.append(submatrix)
        print(submatrix)
    
    return 0

get_submatrix(matrix,n,k)
