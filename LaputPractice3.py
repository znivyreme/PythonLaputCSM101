students = {
    "Ana": [90, 85, 82],
    "Kirk": [72, 73, 78],
    "Liza": [69, 71, 83]
}
highest = 0
namehighest = ""
lowest = float("inf")
namelowest = ""
tally = 0
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, *grades, "Average:", f"{average:.2f}")
    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name
    for grade in grades:
        if grade < 75:
            tally = tally + 1
print(f"\nStudent {namelowest} got the lowest average: {lowest:.2f}")
print(f"Student {namehighest} got the highest average: {highest:.2f}")
print(f"There are {tally} grades which are below 75.")
