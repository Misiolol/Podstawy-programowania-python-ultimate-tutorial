def solution(arr, n: int, m: int):
    x, y = len(arr), len(arr[0])
    for i in range(x - n + 1):
        for j in range(y - m + 1):
            is_zeroes = True
            for k in range(n):
                for l in range(m):
                    if arr[i + k][j + l] != 0:
                        is_zeroes = False
                        break
                if not is_zeroes:
                    break
            if is_zeroes:
                return True
    return False

def main():
    x,y,n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(x)]
    if solution(arr, n, m):
        print("True")
    else:
        print("False")
        
main()

