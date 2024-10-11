def if_difference_one(arr, n):
    for i in range(n-1):
        if arr[i+1] - arr[i] == 1:
            return True
    return False

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if if_difference_one(arr, n):
    print("YES")
else:
    print("NO")

