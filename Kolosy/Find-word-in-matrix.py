n, m = input().split()
n = int(n)
m = int(m)
s = input()
sa = s[::-1] 

arr = []
for _ in range(n):
    a = input()
    arr2 = []
    for char in a:
        arr2.append(char)
    arr.append(arr2)
    
#print(arr)

def if_in_arr(arr, s):
    word_len = len(s)
    
    #? checking each row for the word
    for i in range(n):
        for j in range(m - word_len + 1): 
            if arr[i][j:j + word_len] == list(s):  
                return 1
    
    #? checking each column for the word
    for j in range(m):
        for i in range(n - word_len + 1):
            match = True
            for k in range(word_len):
                if i+k > n:
                        break
                if arr[i + k][j] != s[k]:
                    match = False
                    break
            if match:
                return 1

    return 0  


if if_in_arr(arr, s) or if_in_arr(arr, sa):
    print("YES")
else:
    print("NO")