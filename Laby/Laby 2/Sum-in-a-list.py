arr = input().split()
space_between = input().split()
solution = 0
for i in range (int(space_between[0]), int(space_between[1])+1):
    x = int(arr[i])
    solution+=x

print(solution)

