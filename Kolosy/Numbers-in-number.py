from collections import Counter

def printing(n, s):
    #?creating an array with all numbers
    arr = []
    for char in n:
        arr.append(char)
    
    #? creating boundles 
    boundles = []
    for _ in range(len(arr)-s + 1):
        sub_boundle = ""
        for i in range(_, _+s):
            sub_boundle+=arr[i]
        boundles.append(sub_boundle)
    #print(boundles)        
    
    ctr = Counter(boundles)
    max_apperance = max(ctr.values())
    #print(max_apperance)
    to_print = [num for num, count in ctr.items() if count == max_apperance]
    to_print.sort()
    print(to_print[0])
    
    
def main():
    n = input()
    size = len(n) + 1
    for _ in range(1,size):
        printing(n, _)

main()
    
    