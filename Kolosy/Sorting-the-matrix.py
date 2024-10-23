
def solution(arr):
    digits = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            digits.append(arr[i][j])
    digits.sort()
    k = 0
    #~~ debbuging print(digits)
    for i in range(len(arr)):
        k=i
        for j in range(len(arr[0])):
            print(digits[k], end=" ")
            k+=len(arr)
        print("")
    return 0


def main():
    n,m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    solution(matrix)

main()
