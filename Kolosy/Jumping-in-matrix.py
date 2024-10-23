import _Functions

def move_to_column(arr,x,y):
    sub_arr = []
    for i in range(len(arr)):
        sub_arr.append(arr[i][y])
    if arr[x][y] == min(sub_arr):
        return -1
    else:
        move_to = 0
        for i in range(len(arr)):
            if arr[i][y] == min(sub_arr):
                move_to = i
        return move_to  
    
def move_to_row(arr,x,y):
    sub_arr = []
    for i in range(len(arr)):
        sub_arr.append(arr[x][i])
    if arr[x][y] == min(sub_arr):
        return -1
    else:
        move_to = 0
        for i in range(len(arr)):
            if arr[x][i] == min(sub_arr):
                move_to = i
        return move_to  
      
def solution(arr,x,y):
    markerx, markery = x,y
    while True:
        k = move_to_row(arr,markerx, markery)
        if k != -1:
            markery = k
        k2 = move_to_column(arr,markerx, markery)
        if k2!=-1:
            markerx = k2
        if k == -1 and k2 == -1:
            return [markerx, markery]


def main():    
    size = int(input())
    x,y = map(int, input().split())
    
    matrix = [list(map(int, input().split())) for _ in range(size)]
    point = solution(matrix,x,y)
    print('{} {}'.format(
        point[0],
        point[1]
    ))
    _Functions.matrix_print(matrix)
    return 0

main()