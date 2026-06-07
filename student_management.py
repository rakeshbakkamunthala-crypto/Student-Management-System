students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")

        students[roll] = name

        print("Student Added Successfully")

    elif choice == "2":
        print("\nStudent Records")

        for roll, name in students.items():
            print("Roll:", roll, "Name:", name)

    elif choice == "3":
        roll = input("Enter Roll No: ")

        if roll in students:
            print("Name:", students[roll])
        else:
            print("Student Not Found")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")