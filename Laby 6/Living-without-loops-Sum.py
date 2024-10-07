arr = input().split()

def from_array(i):
    if i < len(arr):
        return from_array(i+1) + int(arr[i])
    return 0

print(from_array(0))