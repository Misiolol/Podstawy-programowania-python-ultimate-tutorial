x,y,n,m = map(int, input().split())

wall = [list(map(int, input().split())) for _ in range(x)]

print(wall[0][0])

def a():
    return 0