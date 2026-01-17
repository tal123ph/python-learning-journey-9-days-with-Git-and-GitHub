# Program to determine grade based on marks using 'if-elif-else'

marks = 85

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Marks: {marks}, Grade: {grade}")
