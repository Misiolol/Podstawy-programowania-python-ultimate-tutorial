arr = input().split()

def sum_from_array(i):
    if i < len(arr):
        return sum_from_array(i+1) + int(arr[i])
    return 0
    
print(sum_from_array(0))