print("===== Student Grade System =====")

math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = math + science + english
average = total / 3

print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"

print("Final Grade:", grade)


