#Using the fact that three points will be on the same line if area of the triangle builded up from those points will be equal to 0


def area_of_triangle(x1, y1, x2, y2, x3, y3):
    area = x1 * (y2 - y3) + x2 * (y3     - y1) + x3 * (y1 - y2)
    return area

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if area_of_triangle(x1, y1, x2, y2, x3, y3) == 0:
    print("True")
else:
    print("False")
