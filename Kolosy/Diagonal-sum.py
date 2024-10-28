import copy
n, m = map(int, input().split())

matrix =  []
for _ in range(n): matrix.append(list(map(int, input().split())))

def adding_zeroes(arr,n):
    k = n-1
    j = n-1
    for i in range(len(arr)):
        sub = copy.deepcopy(arr[i])
        for _ in range(k):
            sub.insert(0,0)
        for _ in range(j):
            sub.append(0)
        arr[i] = sub
        
        
def sum_for_every_in_base(arr):
    sums = []
    for i in range(len(arr[0])):
        temp_sum = 0
        k = i
        for j in range(len(arr)):
            temp_sum+=arr[j][k]
            k+=1
            if k>=len(arr[0]):
                break
        sums.append(temp_sum) 
    for i in range(len(arr[0])-1, 0, -1):
        temp_sum = 0
        k = i
        for j in range(len(arr)):
            temp_sum+=arr[j][k]
            k-=1
            if k>=len(arr[0]):
                break
        sums.append(temp_sum) 
    return sums


adding_zeroes(matrix,n)  
#_Functions.matrix_print(matrix)  
list_of_sums = sum_for_every_in_base(matrix)
print(max(list_of_sums))
