n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)


def calculating_area(point1, point2, point3):
    area = float(abs(point1[0]*(point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1])))
    return area/2

solutions = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if calculating_area(points[i], points[j], points[k]) > 0:
                solutions.append(calculating_area(points[i], points[j], points[k]))
                
print(min(solutions), end=" ")
print(max(solutions))