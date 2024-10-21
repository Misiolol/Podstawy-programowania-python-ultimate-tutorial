matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)
    
    
def if_capable_rows(arr):
    capable = True
    for row in arr:
        nums = set()
        for digit in row:
            nums.add(digit)
        if len(nums) != 9:
            return False
    return True
        
        
def if_capable_columns(arr):
    for j in range(9):
        nums = set()
        for i in range(9):
            nums.add(arr[i][j])
        if len(nums) != 9:
            return False
    return True

def if_capable_diagonal(arr):
    nums = set()
    for i in range(9):
        nums.add(arr[i][i])
        #print(nums, end=" "); print(len(nums))
    if len(nums) != 9:
        #print("a")
        return False 
    else:
        #print("a1")
        nums2 = set()
        j = 0
        for i in range(8, -1, -1):
            nums2.add(arr[i][j])
            j+=1
            #print(nums2)
        if len(nums2) != 9:
            return False
        else:
            return True
    
    
        
        
def if_sudoku_valid(arr):
    if if_capable_columns(arr) and if_capable_rows(arr) and if_capable_diagonal(arr):
        print("X")
    elif if_capable_columns(arr) and if_capable_rows(arr):
        print("True")
    else:
        print("False")
        
if_sudoku_valid(matrix)
