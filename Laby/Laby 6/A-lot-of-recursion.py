dick = {}
def rek(n:int):
    global dick
    if n == 1:
        return 1
    if n in dick.keys():
        return dick[n]
    sol = 1 + rek(n-rek(rek(n-1)))
    dick[n] = sol
    return sol

n = int(input())



print(rek(n))

