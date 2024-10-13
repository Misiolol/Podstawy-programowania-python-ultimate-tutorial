n, m = map(int, input().split())

matrix =  []
for _ in range(n): matrix.append(list(map(int, input().split())))

for i in range(n, 0, -1):
    diagonal_sum = 0
    for j in range(m):
        diagonal_sum+=matrix[i][m]