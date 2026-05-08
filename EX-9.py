M1=int(input("Enter marks for the first subject: "))
M2=int(input("Enter marks for the second subject: "))
M3=int(input("Enter marks for the third subject: "))
M4=int(input("Enter marks for the fourth subject: "))
total_marks =M1+M2+M3+M4
average_marks =total_marks/4
print(f"\nTotal Marks: {total_marks}")
print(f"Average Percentage: {average_marks:.2f}%")
if average_marks >=75:
    grade = 'DISITINCTION'
elif average_marks >=60:
    grade = 'FIRST DIVISION'
elif average_marks >=50:
    grade = 'SECOND DIVISION'
elif average_marks >=40:
    grade = 'THIRD DIVISION'
else:
    grade = 'FAIL'
print(f"Grade: {grade}")
