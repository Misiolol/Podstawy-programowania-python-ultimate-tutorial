solution_array = []

def passed_by_cheating(arr, i, j):
    sum_chating = 0
    sum_chating = float(sum_chating)
    if i > 0 and i < len(arr)-1 and j > 0 and j < len(arr[i])-1:sum_chating = (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]);num = 8
    elif i == 0 and j == 0: sum_chating = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1];num = 3
    elif i == 0 and j == len(arr[i])-1: sum_chating = arr[i][j-1] + arr[i+1][j] + arr[i+1][j-1];num = 3
    elif i == len(arr)-1 and j == 0: sum_chating = arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1];num = 3
    elif i == len(arr)-1 and j == len(arr[i])-1: sum_chating = arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1];num = 3
    elif i == 0 and j > 0 and j < len(arr[i])-1: sum_chating = (arr[i][j-1] + arr[i][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]);num = 5
    elif i == len(arr)-1 and j > 0 and j < len(arr[i])-1: sum_chating = (arr[i][j-1] + arr[i][j+1] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]);num = 5
    elif j == 0 and i > 0 and i < len(arr)-1: sum_chating = (arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]);num = 5
    elif j == len(arr[i])-1 and i > 0 and i < len(arr)-1: sum_chating = (arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1] + arr[i+1][j] + arr[i+1][j-1]);num = 5 
    return float(sum_chating/num) >= 3
        
def passed_by_cheating_wrong_one(arr, i, j):
    sum_chating = 0.0
    num = 0
    rows = len(arr)
    cols = len(arr[0])

    #? Loop over the neighbors (3x3 grid around the element arr[i][j])
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            #? Skip the center element (arr[i][j])
            if x == i and y == j:
                continue
            #? Make sure the indices are within bounds
            if 0 <= x < rows and 0 <= y < cols:
                sum_chating += arr[x][y]
                num += 1

    #! Return whether the average of the surrounding values is greater than 3
    return float(sum_chating / num) > 3 if num > 0 else False

def if_pass(arr, i, j):
    global solution_array
    avg = arr[i][j]
    if avg>=3:
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