# Simple Student Grade Calculator

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("\nStudent:", name)
print("Marks:", marks)
print("Grade:", grade)