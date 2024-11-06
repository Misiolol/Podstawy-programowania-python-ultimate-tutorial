def is_divider(digit: int, d: int):
    if digit % d == 0:
        return 1
    return 0

def if_perfect(digit: int):
    sum_of_divisors = 0 
    for i in range(1, digit-1):
        if is_divider(digit, i):
            sum_of_divisors += i
        
    if sum_of_divisors == digit:
        return True
    return False


n = int(input())
perfect = []
arr = list(map(int, input().split()))
#print(arr)
for digit in arr:
    #print(digit)
    if if_perfect(digit):
        perfect.append(digit)

arr.sort(reverse=True)
perfect.sort(reverse=True)
print(arr)
print(perfect)
