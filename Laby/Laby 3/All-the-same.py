number_of_digits = int(input())
arr = []
for _ in range(number_of_digits):
    arr.append(int(input()))
arr.sort()
if(arr[0] == arr[len(arr)-1]):
    print("True")
else:
    print("False")