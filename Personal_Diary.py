import os

# Function to display the menu
def display_menu():
    print("\n--- Personal Diary ---")
    print("1. Write a new entry")
    print("2. View previous entries")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    return choice

# Function to write a new entry to the diary file
def write_entry(file_name):
    try:
        with open(file_name, 'a') as file:
            print("\nEnter your daily thoughts (Type 'exit' to stop):")
            while True:
                entry = input("Your thoughts: ")
                if entry.lower() == 'exit':
                    break
                file.write(entry + "\n")
            print("Your entry has been saved.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to view previous entries from the diary file
def view_entries(file_name):
    try:
        if not os.path.exists(file_name):
            print("\nNo diary entries found.")
            return

        with open(file_name, 'r') as file:
            entries = file.readlines()
            if entries:
                print("\n--- Previous Entries ---")
                for entry in entries:
                    print(entry.strip())
            else:
                print("\nNo entries to display.")
    except FileNotFoundError:
        print("Error: Diary file not found.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to run the diary application
def main():
    file_name = "diary.txt"  # File where diary entries are stored
    while True:
        choice = display_menu()
        if choice == '1':
            write_entry(file_name)
        elif choice == '2':
            view_entries(file_name)
        elif choice == '3':
            print("\nThank you for using the Personal Diary. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
