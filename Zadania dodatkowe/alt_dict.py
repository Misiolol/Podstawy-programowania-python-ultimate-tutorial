from collections import Counter

k = int(input())
arr = []
for _ in range(k):
    arr.append(int(input()))

l = Counter(arr)
print(l)