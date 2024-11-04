def all_substrings(input):
    arr = []
    for i in range(1,len(input)):
        subs = []
        for j in range(len(input)):
            if len(input[j:j+i]) == i:
                subs.append(input[j:j+i]) 
        arr.append(subs)
    arr.append([input])
    #print(arr)
    return arr

def if_palindr00me(number):
    number = number.rstrip('0')
    if number == number[::-1] and len(number) > 0:
        return True
    return False



def solution(arr):
    ct = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if if_palindr00me(arr[i][j]):
                ct += 1    
    print(ct)
    return 0
N = input()
solution(all_substrings(N))

