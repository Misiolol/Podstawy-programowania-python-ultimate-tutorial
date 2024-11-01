n = int(input())

students = []

degrees = []

for _ in range(n):
    row = input().split()
    studenci = row[0]
    oceny = row[1:]
    
    suma_ocen = 0
    for ocena in oceny:
        test, wartosc = ocena.split(':')
        wartosc = float(wartosc)
        suma_ocen += wartosc
        if test in [nazwa[0] for nazwa in degrees]:
            for i in range(len(degrees)):
                if degrees[i][0] == test:
                    degrees[i][1].append(wartosc)
                    break
        else:
            degrees.append([test, [wartosc]])
    students.append([studenci, suma_ocen/len(oceny)])
for student in sorted([s[0] for s in students]):
    print('{} {}'.format(
        student,
        students[[s[0] for s in students].index(student)][1]
    ))
for degree in sorted([d[0] for d in degrees]):
    values = degrees[[d[0] for d in degrees].index(degree)][1]
    print('{} {}'.format(
        degree,
        sum(values)/len(values)
    ))