def if_sliceable(arr):
    if len(arr) < 2:
        return True
    arr.sort()
    l = arr[1] - arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != l:
            return False
    return True

arr = list(map(int, input().split()))
if if_sliceable(arr):
    print("True")
else:
    print("False")
