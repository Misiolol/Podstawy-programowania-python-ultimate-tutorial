n, m = map(int, input().split())  
arr = list(map(int, input().split()))


for i in range(m):
    x, y = map(int, input().split()) 
    arr[x], arr[y] = arr[y], arr[x]

print(" ".join(map(str, arr)))