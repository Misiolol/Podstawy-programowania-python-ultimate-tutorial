def calculate_grade(pts, max_pts):
    if max_pts == 0:
        return 0
    percentage = pts / max_pts * 100
    if percentage < 50:
        return 2
    elif percentage < 70:
        return 3
    elif percentage < 90:
        return 4
    else:
        return 5

def round_final_grade(average):
    if average < 3:
        return 2
    elif average < 3.5:
        return 3
    elif average < 4.5:
        return 4
    else:
        return 5

def main():
    n, m = map(int, input().split())
    students = {}

    for _ in range(n):
        name, index = input().split()
        students[name] = []

    for _ in range(m):
        test = input().split()
        
        if test[0].isalpha():
            name = test[0]
            index = test[1]
            pts, max_pts = map(int, test[2].split('/'))
        else:
            index = test[0]
            name = test[1]
            pts, max_pts = map(int, test[2].split('/'))
        
        grade = calculate_grade(pts, max_pts)
        students[name].append(grade)

    sorted_students = sorted(students.keys())

    for name in sorted_students:
        grades = students[name]
        if grades:
            avg_grade = sum(grades) / len(grades)
            final_grade = round_final_grade(avg_grade)
            print(f"{name} {final_grade}")
        else:
            print(f"{name} 2")

main()
