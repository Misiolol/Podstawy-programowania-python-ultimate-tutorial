t = int(input())

solution = []
for i in range(t):
    arr = list(map(int, input().split()))
    m = arr[1]
    a = arr[0]
    counter = 1
    bal = a 
    while bal<m:
        a*=2
        bal+=a  
        counter+=1
    solution.append(counter)

for days in solution:
    print(days)