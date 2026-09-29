patients = {
    "Ana": [90, 100, 110, 120, 130, 140, 150],
    "Ben": [190, 180, 167, 162, 99, 82, 77]
}
for name, values in patients.items():
    print("--------")
    print(name)
    print("--------")
    for sugar in values:
        if sugar >= 120:
            print(sugar, ":(High Blood Sugar)")
        else:
            print(sugar, ":(Normal Blood Sugar)")
    mx = max(values)
    mm = min(values)
    avr = sum(values) / len(values)
    diff = mx - mm
    print("Max:", mx)
    print("Min:", mm)
    print("Average:", avr)
    print("Difference:", diff)
