def grade_cal(marks):
    if marks >= 90:
        grade = "A"
    elif marks>=80 and marks<90:
        grade = "B"
    elif marks>=70 and marks<80:
        grade = "C"
    elif marks<70:
        grade = "F"
    else:
        print("Marks should be b/w 0 to 100")
    print(grade)
        