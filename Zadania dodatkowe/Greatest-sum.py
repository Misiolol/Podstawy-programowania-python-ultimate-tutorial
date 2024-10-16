n = int(input())

arr = []
for _ in range(n):
    digit = int(input())
    arr.append(digit)

max_sum = 0
indexes = []
for i in range(len(arr)-2):
    sum_of_three = arr[i] + arr[i+1] + arr[i+2]
    if sum_of_three > max_sum:
        max_sum = sum_of_three
        indexes = [i, i+1, i+2]

print(arr)

solution_array = []
for i in range(len(arr)):
    if i not in indexes:
        solution_array.append(arr[i])

print(solution_array)