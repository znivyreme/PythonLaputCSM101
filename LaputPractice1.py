students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 75,
}
print("STUDENTS GRADE")
print("--------------")
print("Ana: ", students["Ana"])
print("Ben: ", students["Ben"])

students["Ella"] = 88
students["Ana"] = 82
students["Ben"] = 91
name1 = input("Enter student name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("--------------")
for name, grade in students.items():
    print(name, ":", grade)
search = input("Enter student name to: ")
if search in students:
    print(search, ":", students[search])
else:
    print("Student not found")
