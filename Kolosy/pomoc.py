L = input().split()

L = list(map(int,L))
#print(L)
L.sort()

n = len(L)
if n == 1:
    print("True")
else:    
    r = L[1]-L[0]
    Nth = lambda n:L[0]+(n-1)*r
    K = list(map(Nth,range(1,n+1,1)))
    K = list(map(int,K))
    #print(K)


    d=0
    for U in range(n):
        if(L[U]!=K[U]):
            print("False")
            
            break

        elif(U==n-1):
            print("True")