
print("=== Student Grade Calculator ===")

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
