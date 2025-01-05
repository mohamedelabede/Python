class Student:
    def __init__(self, name, age, grades):
        self.name = name  
        self.age = age    
        self.grades = grades  
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def add_grade(self, grade):
        self.grades.append(grade)


class StudentDatabase:
    def __init__(self):
        self.students = []  # List to hold student objects

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print(f"Average Grade: {student.average_grade():.2f}\n")

    def find_student_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None


# Example usage
if __name__ == "__main__":
    student1 = Student("Alice", 20, [85, 90, 88])
    student2 = Student("Bob", 22, [70, 75, 78])
    student3 = Student("Charlie", 21, [92, 95, 98])

    student_db = StudentDatabase()
    student_db.add_student(student1)
    student_db.add_student(student2)
    student_db.add_student(student3)
    student_db.display_all_students()
    student_db.find_student_by_name("Bob").add_grade(80)
    print("\nUpdated Student Info:")
    student_db.find_student_by_name("Bob").display_info()
    print(f"Updated Average Grade: {student_db.find_student_by_name('Bob').average_grade():.2f}")
