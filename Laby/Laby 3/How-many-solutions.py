
def main():
    n,x,y = map(int, input().split())

    number_of_solutions = 0
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for m in range(n+1):
                    if x*(i**2 - k**2) + y*(j**2 - m**2) == 0:
                        number_of_solutions += 1
    print(number_of_solutions)

main()