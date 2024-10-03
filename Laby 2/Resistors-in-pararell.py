a = input()
a = int(a)

arr = list(map(float, input().split()))

result = 0
for i in range(a):
    result+=1/arr[i]

print(1/result)
