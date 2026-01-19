#import os library
import os

#function for grade marks
def gradeSystem(marks):
    try:
        if marks>=90:
            return "Grade A"
        elif marks>=80:
            return "Grade B"
        elif marks>=70:
            return "Grade C"
        elif marks>=60:
            return "Grade D"
        elif marks>=50:
            return "Grade E"
        else:
            return "Fail"
    except Exception as error:
        print(error)



def main():
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    grade = gradeSystem(marks)

    #open file in write mode
    with open("student_grades.txt", "a") as file:
        result = f"{name} - {grade}"
        file.write(result + "\n")
        print(f"Recorded: {result}")
main()
