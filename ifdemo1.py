marks = int(input("enter marks"))
if marks > 75:
    grade="distinction"
elif marks <= 75 and marks > 60 :
    grade="first"
elif marks <=60 and marks > 50:
    grade = "second"
elif marks <=50 and marks > 35:
    grade = "third"
else:
    grade="fail"
    
#it is outside if..elif..else
if grade!="fail":
    print("you pass the exam with grade ",grade)
else:
    print("You fail the exam with grade ",grade)
