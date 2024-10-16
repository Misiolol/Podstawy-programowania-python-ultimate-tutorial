n = int(input())

max_len = 0
words = []
for _ in range(n):
    word = input()
    words.append(word)
    if max_len < len(word):
        max_len = len(word)

arr = []
for i in range(max_len):
    arr.append([])

for word in words:
    current_size = len(word)
    arr[current_size-1].append(word)

for i in range(max_len):
    arr[i].sort()


for i in range(len(arr)):
    if len(arr[i]) > 0:
        print(arr[i], end = " ")
