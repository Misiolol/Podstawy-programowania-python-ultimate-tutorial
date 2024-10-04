def smallest_divisor(n:int):
    for i in range (2,n):
        if n%i == 0:
            return i
def main():
    n = int(input())
    print(smallest_divisor(n))

main()


    