name = input("Enter student name: ")

mark1 = float(input("Enter marks in Subject 1: "))

if mark1 > 100:
    print("Error: Marks cannot exceed 100.")
    exit()

mark2 = float(input("Enter marks in Subject 2: "))

if mark2 > 100:
    print("Error: Marks cannot exceed 100.")
    exit()

mark3 = float(input("Enter marks in Subject 3: "))

if mark3 > 100:
    print("Error: Marks cannot exceed 100.")
    exit()

mark4 = float(input("Enter marks in Subject 4: "))

if mark4 > 100:
    print("Error: Marks cannot exceed 100.")
    exit()

total = mark1 + mark2 + mark3 + mark4
average = total / 4

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)