def compare(a: int,b: int):
    if a>b:
        return 1
    if b>a:
        return 2
    if a==b:
        return 3

def main():
    number_of_tests = int(input())
    arr = []
    solutions = []
    for _ in range (number_of_tests):
        a,b = map(int, input().split())
        arr.append((a,b))

    for i in range(len(arr)):
        if compare(arr[i][0], arr[i][1]) == 1:
            solutions.append(f"{arr[i][0]}  is greater than  {arr[i][1]}")
        if compare(arr[i][0], arr[i][1]) == 2:
            solutions.append(f"{arr[i][0]}  is smaller than  {arr[i][1]}")
        if compare(arr[i][0], arr[i][1]) == 3:
            solutions.append(f"n is equal m:  {arr[i][1]}")
    
    for i in range(len(solutions)):
        print(solutions[i])

main()
