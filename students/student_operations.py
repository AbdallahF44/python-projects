import json


def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def add_student(students, student):
    students[student["id"]] = student
    print(f"Student {student['name']} added successfully.")
    return students


def show_students(students):
    if not students:
        print("No students found")
        return
    for student in students.values():
        print(
            f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Major: {student['major']}"
        )


def search_for_student(students, id_for_search):
    return students.get(id_for_search)


def update_student(students):
    id_for_update = input("Enter the ID of the student to update: ")
    student_to_update = search_for_student(students, id_for_update)
    if student_to_update:
        print(
            f"ID: {student_to_update['id']}, Name: {student_to_update['name']}, Age: {student_to_update['age']}, Major: {student_to_update['major']}"
        )
        new_name = input("*****\nEnter new name (leave blank to keep current value): ")
        new_age = input("Enter new age (leave blank to keep current value): ")
        new_major = input("Enter new major (leave blank to keep current value): ")
        if new_name:
            student_to_update["name"] = new_name
        if new_age:
            student_to_update["age"] = int(new_age)
        if new_major:
            student_to_update["major"] = new_major
        students[id_for_update] = student_to_update
        print("Student updated successfully.")
    else:
        print("Student not found.")
    return students


def delete_student(students, id_for_delete):
    if id_for_delete in students:
        del students[id_for_delete]
        print("Student deleted successfully.")
    else:
        print("Student not found.")
    return students
