from student_operations import (
    save_students,
    add_student,
    search_for_student,
    show_students,
    update_student,
    delete_student,
)
import json

try:
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = {}
while True:
    print("*" * 35)
    print("Enter 1 to add a student")
    print("Enter 2 to view all students")
    print("Enter 3 to search for a student")
    print("Enter 4 to update a student")
    print("Enter 5 to delete a student")
    print("Enter 6 to exit")
    try:
        choice = int(input("Enter your choice: "))
        print("*" * 15)
        if choice == 1:
            student = {}
            student["id"] = input("Enter student ID: ")
            if student["id"] in students:
                print("Student ID already exists.")
                continue
            student["name"] = input("Enter student name: ")
            student["age"] = int(input("Enter student age: "))
            student["major"] = input("Enter student major: ")
            print("*" * 15)
            students = add_student(students, student)
            save_students(students)
        elif choice == 2:
            show_students(students)
        elif choice == 3:
            id_for_search = input("Enter ID for search: ")
            result = search_for_student(students, id_for_search)
            if result:
                print(
                    f"ID: {result['id']}, Name: {result['name']}, Age: {result['age']}, Major: {result['major']}"
                )
            else:
                print("Student not found.")
        elif choice == 4:
            students = update_student(students)
            save_students(students)
        elif choice == 5:
            id_for_delete = input("Enter the ID of the student to delete: ")
            students = delete_student(students, id_for_delete)
            save_students(students)
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
