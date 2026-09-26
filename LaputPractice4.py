students = {}
number = int(input("Enter number of students: "))
for i in range(number):
    print("\nStudent", i + 1)
    name = input("Enter Student name: ")
    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))
    students[name] = (grade1, grade2, grade3)
print("\n======= STUDENT RECORDS ========")

for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, *grades, "Average:", round(average, 2))
highest = 0
namehighest = ""
tally = 0

for name, grades in students.items():
    average = sum(grades) / len(grades)

    if average > highest:
        highest = average
        namehighest = name

    for g in grades:
        if g < 75:
            tally += 1


print(f"\nStudent {namehighest} got the highest average: {highest:.2f}")
print(f"There are {tally} grades which are below 75.")