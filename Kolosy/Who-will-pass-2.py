solution_array = []

def passed_by_cheating(arr, x, y):
    #? getting the column avg
    nums = []
    for i in range(len(arr[x])):
        if arr[x][i] >= arr[x][y] and i!=y:
            nums.append(arr[x][i])
    for i in range(len(arr)):
        if arr[i][y] >= arr[x][y] and i!=x:
            nums.append(arr[i][y])
    nums.append(arr[x][y])
    return float(sum(nums)/len(nums)) >= 7

def if_pass(arr, i, j):
    global solution_array
    avg = arr[i][j]
    if avg>=7:
        solution_array[i][j]=1
    else:
        if passed_by_cheating(arr, i, j):
            solution_array[i][j]=1

def matrix_print(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    print(" ")

def main():
    global solution_array
    n = int(input())
    matrix = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    for _ in range(n):
        row = []
        for l in range(n):
            row.append(0)
        solution_array.append(row)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if_pass(matrix,i,j)

    matrix_print(solution_array, n,n)
    

main()