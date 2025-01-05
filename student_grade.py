import os
def display_menu():
    print("\n--- Grade Tracker ---")
    print("1. Enter grades for subjects")
    print("2. View and calculate average grade")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    return choice

def enter_grades(file_name):
    grades = []
    while True:
        try:
            subject = input("\nEnter the subject name (or type 'done' to finish): ").strip()
            if subject.lower() == 'done':
                break
            grade = float(input(f"Enter the grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Error: Please enter a grade between 0 and 100.")
                continue
            grades.append((subject, grade))
        except ValueError:
            print("Invalid input. Please enter a valid grade (numeric).")
    
    try:
        with open(file_name, 'a') as file:
            for subject, grade in grades:
                file.write(f"{subject}: {grade}\n")
        print("Grades have been successfully saved.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred while saving grades: {e}")

def view_and_calculate_average(file_name):
    if not os.path.exists(file_name):
        print("No grades have been entered yet.")
        return
    
    grades = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    subject, grade = line.strip().split(':')
                    grades.append(float(grade.strip()))
                except ValueError:
                    print(f"Error: Failed to parse the line '{line.strip()}'. Skipping.")
    
        if grades:
            average = sum(grades) / len(grades)
            print(f"\n--- Grades Summary ---")
            for line in open(file_name, 'r'):
                print(line.strip())
            print(f"\nAverage Grade: {average:.2f}")
        else:
            print("No valid grades to calculate average.")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    file_name = "grades.txt"
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            enter_grades(file_name)
        elif choice == '2':
            view_and_calculate_average(file_name)
        elif choice == '3':
            print("\nThank you for using the Grade Tracker. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
