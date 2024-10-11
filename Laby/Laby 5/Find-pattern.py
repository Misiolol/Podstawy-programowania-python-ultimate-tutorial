def if_pattern(s, p):
    #
    #*  error handling (nie pomogl)
    #

    if len(p) == 0:  
        return True
    if len(s) < len(p):  
        return False
    

    for i in range(len(s) - len(p)+1):
        substring = ""
        for j in range(i, i+len(p)):
            substring += s[j]
            #print(substring)
        if substring == p:
            return True
    return False

# rozwiazanie algorytmiczne na gorze a dla studenta (debila) na dole
#! if_pattern() wypierdala runtime error w niektórych case'ach
# nie wiem czemu i nie chce wiedziec 


def if_pattern2(s,p):
    return p in s


s = input()
p = input()

if if_pattern2(s, p):
    print("YES")
else:
    print("NO")
