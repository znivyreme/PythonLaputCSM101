students = {"Ana":[90,85,82],
            "Kirk": [72,73,78]}
studentstuple = {"Ana": (90, 85, 82),
                "Kirk": (72, 73, 78)}
print("Dictionary to List")
for name, grade in students.items():
    print(name, *grade)
print("Dictionary to Tuple")
for name, grade in students.items():
        print(name, *grade)
