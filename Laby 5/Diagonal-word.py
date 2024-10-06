n = int(input())
arr = []
for _ in range(n):
    word = input()
    arr.append(word)


for i in range(n):
    print(arr[i][i], end='')