import json
import os

class StudentManagement:

    def __init__(self):
        self.file = "students.json"
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.students, f)

    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")

        self.students[roll] = name
        self.save_data()

        print("Student Added Successfully")

    def view_students(self):
        if not self.students:
            print("No Students Found")
        else:
            print("\nStudent Records")
            for roll, name in self.students.items():
                print("Roll:", roll, "Name:", name)

    def search_student(self):
        roll = input("Enter Roll No: ")

        if roll in self.students:
            print("Name:", self.students[roll])
        else:
            print("Student Not Found")

    def update_student(self):
        roll = input("Enter Roll No to Update: ")

        if roll in self.students:
            new_name = input("Enter New Name: ")
            self.students[roll] = new_name
            self.save_data()

            print("Student Updated Successfully")
        else:
            print("Student Not Found")

    def delete_student(self):
        roll = input("Enter Roll No to Delete: ")

        if roll in self.students:
            del self.students[roll]
            self.save_data()

            print("Student Deleted Successfully")
        else:
            print("Student Not Found")


obj = StudentManagement()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.view_students()

    elif choice == "3":
        obj.search_student()

    elif choice == "4":
        obj.update_student()

    elif choice == "5":
        obj.delete_student()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
