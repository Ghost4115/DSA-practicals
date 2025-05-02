# Name: Manav Uttekar
# Roll no: 71
# Problem Statement: Department maintains student information. The file
# contains roll number, name, division, and address. Allow user to add, delete 
# information of a student. Display information of a particular student.
# If the record of the student does not exist, an appropriate message is displayed.
# If it does exist, then the system displays the student details. Use sequential file 
# to maintain the data.

import os

FILENAME = "students.txt"

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    division = input("Enter Division: ")
    address = input("Enter Address: ")
    with open(FILENAME, "a") as file:
        file.write(f"{roll_no},{name},{division},{address}\n")
    print("Student record added successfully!")

def display_student():
    roll_no = input("Enter Roll Number to search: ")
    found = False
    if not os.path.exists(FILENAME):
        print("No student records found.")
        return
    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll_no:
                print("\nStudent Found:")
                print(f"Roll No: {data[0]}")
                print(f"Name: {data[1]}")
                print(f"Division: {data[2]}")
                print(f"Address: {data[3]}")
                found = True
                break
    if not found:
        print("Student record not found!")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    found = False
    if not os.path.exists(FILENAME):
        print("No student records found.")
        return
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    with open(FILENAME, "w") as file:
        for line in lines:
            if line.strip().split(",")[0] != roll_no:
                file.write(line)
            else:
                found = True
    if found:
        print("Student record deleted successfully!")
    else:
        print("Student record not found!")

if __name__ == "__main__":
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again!")
