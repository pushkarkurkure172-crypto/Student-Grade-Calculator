



print("=== Student Grade Calculator ===")

total = 0

for i in range(1, 6):
    while True:
        try:
            marks = float(input(f"Enter marks for Subject {i}: "))

            if 0 <= marks <= 100:
                total += marks
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

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
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
