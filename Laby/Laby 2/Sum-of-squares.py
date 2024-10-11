input_a_and_b = input().split()
a = int(input_a_and_b[0])
b = int(input_a_and_b[1])

amount_of_addons = b-a
solution = a*a
for i in range (amount_of_addons):
    a+=1
    solution+=a*a
    #print(a)
print(solution)