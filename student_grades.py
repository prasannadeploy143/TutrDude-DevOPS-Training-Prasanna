# Initialize an empty dictionary to store student data
student_grades = {}

while True:
    # Display a menu of options
    print("\n--- Student Grades Manager ---")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    # Condition 1: Add a new student
    if choice == "1":
        name = input("Enter student name: ")
        if name in student_grades:
            print("Error: Student already exists! Use option 2 to update.")
        else:
            grade = input("Enter student grade: ")
            student_grades[name] = grade
            print(f"Success: Added {name} with grade {grade}.")
            
    # Condition 2: Update an existing student
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            new_grade = input("Enter new grade: ")
            student_grades[name] = new_grade
            print(f"Success: Updated {name}'s grade to {new_grade}.")
        else:
            print("Error: Student not found!")
            
    # Condition 3: Print all grades
    elif choice == "3":
        if not student_grades:
            print("The gradebook is currently empty.")
        else:
            print("\n--- Current Gradebook ---")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")
                
    # Condition 4: Exit the program
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
        
    # Catch invalid menu choices
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
