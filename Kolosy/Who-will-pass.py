solution_array = []

def passed_by_cheating(arr, i, j):
    return 1

def if_pass(arr, i, j):
    global solution_array
    avg = arr[i][j]
    if avg>=3:
        solution_array[i][j]=1
    else:
        if passed_by_cheating(arr, i, j):
            return 1

def main():
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

    print(solution_array)
    print(matrix)

main()