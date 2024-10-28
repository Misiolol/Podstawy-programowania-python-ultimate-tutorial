#import _Functions
def matrix_print(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print("")
    print(" ")


def reverse_row(arr, idx: int):
    sub = []
    sub = arr[idx]
    sub = sub[::-1]
    arr[idx] = sub
    #_Functions.matrix_print(arr)
    return arr

def reverse_column(arr, idx:int):
    sub = []
    for i in range(len(arr)):
        sub.append(arr[i][idx])
    sub.reverse()
    for i in range(len(arr)):
        arr[i][idx] = sub[i]
    return arr

def transchuj(arr):
    subarr = []
    for _ in range(len(arr[0])):
        temp = []
        for k in range(len(arr)):
            temp.append(0)
        subarr.append(temp)

    #print(subarr)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            subarr[j][i] = arr[i][j]

    return subarr
    
def solution(todo, matrix):
    mtx = matrix
    for task in todo:
        if task[0] == "R":
            task,idx = task.split(" ")
        if task == "RR":
            mtx = reverse_row(mtx, int(idx))
        if task == "RC":
            mtx = reverse_column(mtx, int(idx))
        if task == "T":
            mtx = transchuj(mtx)
    return mtx


def main():
    x,y = map(int, input().split())
    matrix = [list(map(str, input().split())) for _ in range(x)]
    n = int(input())
    to_do = []
    for _ in range(n):
        to_do.append(input())
    matrix_print(solution(to_do, matrix))
main()