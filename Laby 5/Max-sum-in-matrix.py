def max_sum_rectangle(matrix, n):
    if not matrix or not matrix[0]:
        return 0

    max_sum = 0

    for xmain in range(1,n+1):
        for ymain in range(1,n+1):
            for xsub in range(n - xmain + 1):
                for ysub in range(n - ymain + 1):
                    current_max = 0
                    for i in range(xsub, xsub + xmain):
                        row_slice = matrix[i][ysub:ysub + ymain]
                        current_max += sum(row_slice)
                    max_sum = max(current_max, max_sum)
    return max_sum


n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

print(max_sum_rectangle(matrix, n))

