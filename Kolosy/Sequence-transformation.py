n,m = map(int, input().split())
s = input()
operations = []
for _ in range(m):
    operations.append(input())


def change(str, change):
    a,b,add = change.split(";")
    a = int(a)
    b = int(b)
    sbs = str[0:min(a,b)]
    sbs+=add
    sbs += str[max(a,b)+1:len(str)]
    return sbs

sa = []
sa.append(s)
k = 0
for _ in range(m):
    sa.append(change(sa[k], operations[_])) 
    k+=1

print(sa[len(sa)-1])


#?counting len of each element and printing the longest

max_len = 0
for _ in range(len(sa)):
    alen = len(sa[_])
    if alen > max_len:
        solution = sa[_]
        max_len = alen
print(solution)