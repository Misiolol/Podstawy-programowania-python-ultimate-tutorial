def sum_of_2(list):
    sums_2 = []
    for i in range(len(list)):
        dif_2 = list[i::2]
        sums_2.append(sum(dif_2))

    sums_2.sort(reverse = True) 
    
    return sums_2
     
def sum_of_3(list):
    sums_3 = []   
    for i in range(len(list)):
        dif_3 = list[i::3]
        sums_3.append(sum(dif_3))
    sums_3.sort(reverse = True)   
    return sums_3

def all_sublists(arr):
    sublists = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if len(arr[i:j]) > 0 : sublists.append(arr[i:j])
    return(sublists)

def solution(sublists):
    smm2 = []
    smm3 = []
    for sublist in sublists:
        sm2 = sum_of_2(sublist)
        sm3 = sum_of_3(sublist)
        smm2.extend(sm2)  
        smm3.extend(sm3)

    solutions = []
    for d in smm2:
        for k in smm3:
            if d == k:
                solutions.append(d)
    return max(solutions)
    
def main():
    k = int(input())
    arr = list(map(int, input().split()))
    if k == 1:
        print(arr[0])
    else:    
        print(solution(all_sublists(arr)))
    
    
main()