subjects = int(input("Enter number of subjects: "))

if subjects <= 0:
    print("Number of subjects must be greater than 0.")
else:
    total = 0
    valid = True

    for i in range(subjects):
        marks = float(input(f"Enter marks for subject {i + 1} (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            valid = False
            break

        total += marks

    if valid:
        percentage = total / subjects

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print("\n--- Student Grade Report ---")
        print("Total Marks:", total, "/", subjects * 100)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
