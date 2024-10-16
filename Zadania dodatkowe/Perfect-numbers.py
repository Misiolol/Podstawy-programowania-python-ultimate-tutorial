def if_perfect(digit):
    sum_of_divisors = 0 
    for i in range(1, digit-1):
        if digit % i == 0:
            sum_of_divisors += i
        
    if sum_of_divisors == digit:
        return True
    return False


a = int(input())
arr = []
perfect = []
for _ in range(a):
    digit = int(input())
    arr.append(digit)
    if if_perfect(digit):
        perfect.append(digit)

arr.sort(reverse=True)
perfect.sort(reverse=True)
print(arr)
print(perfect)
