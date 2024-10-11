height = int(input())
number_of_segments = int(input())

for i in range(1, height+1):
    print(i*"* ")

actual_heaight = height+1
for i in range(number_of_segments-1):
    for j in range (1, actual_heaight+1):
        print(j*"* ")
    actual_heaight+=1
