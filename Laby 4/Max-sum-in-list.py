def main():
    arr = list(map(int, input().split()))

    solution = 0   #<--- max continious sum
    for i in range(len(arr)):
        current_sum = 0 
        for j in range(i, len(arr)):
            current_sum+=arr[j]
            if current_sum > solution:
                solution = current_sum

    if solution < 0:
        solution = 0
    print(solution)


main()