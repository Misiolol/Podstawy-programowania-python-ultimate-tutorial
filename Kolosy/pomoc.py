n=int(input());students=[];degrees=[];[(students.append([s:=row[0],(suma_ocen:=(sum(float(wartosc) for test, wartosc in (o.split(':') for o in row[1:])))/len(row[1:])]))), [degrees.append([test, [float(wartosc)]]) if test not in [d[0] for d in degrees] else [d[1].append(float(wartosc)) for d in degrees if d[0] == test][0] for test, wartosc in (o.split(':') for o in row[1:])]) for row in [input().split()]];print('\n'.join(f'{s[0]} {s[1]}' for s in sorted(students, key=lambda x: x[0])));print('\n'.join(f'{d[0]} {sum(d[1])/len(d[1])}' for d in sorted(degrees, key=lambda x: x[0])))
