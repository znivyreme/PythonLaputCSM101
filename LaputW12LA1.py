laput_class_record ={
    "Dion":{
    "StudID": "11409",
    "Grade": [90, 93, 92, 96, 90, 90, 92]
    },
    "Dungog": {
    "StudID": "11408",
    "Grade": [70, 70, 80, 59, 72, 90, 59]
    },

    "Espinoza": {
    "StudID": "11408",
    "Grade": [90, 94, 59, 92, 98, 90, 100]
    }
}
laput_stud = input("Enter student name: ")
if laput_stud in laput_class_record:
    laput_grd = laput_class_record[laput_stud]["Grade"]
    print("Student found!")
    print("Student ID:", laput_class_record [laput_stud] ["StudID"])
    print("Grades:", laput_grd)
    laputavr = sum(laput_grd)/len(laput_grd)
    print("Average:", laputavr)
    for grade in laput_grd:
        if grade < 60:
            print("Candidate for intervention")
            break
    else:
        print("Highest Grade:", max(laput_grd))
    print("Lowest Grade:", min(laput_grd))
else:
    print("Student not found.")
