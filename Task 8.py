# Task 9: Practice Python Lists With Student Records

student_names = []
student_marks = []

# Get student records
n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i + 1}: ")
    mark = float(input(f"Enter marks for {name}: "))

    student_names.append(name)
    student_marks.append(mark)

# Display all student records
print("\n--- Student Records ---")
for i in range(len(student_names)):
    print(f"Name: {student_names[i]}, Marks: {student_marks[i]}")

# Search for a student
search_name = input("\nEnter a student name to search: ")
if search_name in student_names:
    index = student_names.index(search_name)
    print(f"{search_name} scored {student_marks[index]} marks.")
else:
    print("Student not found.")

# Sort records by marks (highest to lowest)
sorted_records = sorted(
    zip(student_names, student_marks),
    key=lambda record: record[1],
    reverse=True
)

print("\n--- Students Sorted by Marks (Highest to Lowest) ---")
for name, mark in sorted_records:
    print(f"Name: {name}, Marks: {mark}")

# Find highest and lowest scores
if student_marks:
    highest_index = student_marks.index(max(student_marks))
    lowest_index = student_marks.index(min(student_marks))

    print("\n--- Score Results ---")
    print(
        f"Highest score: {student_marks[highest_index]} "
        f"({student_names[highest_index]})"
    )
    print(
        f"Lowest score: {student_marks[lowest_index]} "
        f"({student_names[lowest_index]})"
    )
else:
    print("No student records available.")
