# Name: Manav Uttekar
# Roll no: 71
# Problem Statement: Department maintains student information. The file
# contains roll number, name, division, and address. Allow user to add, delete 
# information of a student. Display information of a particular student.
# If the record of the student does not exist, an appropriate message is displayed.
# If it does exist, then the system displays the student details. Use sequential file 
# to maintain the data.


import os

FILENAME = "students.txt"  # The file where student records are stored

# Function to add a new student record
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    division = input("Enter Division: ")
    address = input("Enter Address: ")
    with open(FILENAME, "a") as file:  # Open the file in append mode to add new data
        file.write(f"{roll_no},{name},{division},{address}\n")
    print("Student record added successfully!")

# Function to display student details
def display_student():
    roll_no = input("Enter Roll Number to search: ")
    found = False
    if not os.path.exists(FILENAME):  # Check if file exists
        print("No student records found.")
        return
    with open(FILENAME, "r") as file:  # Open the file in read mode
        for line in file:
            data = line.strip().split(",")  # Split the data by commas
            if data[0] == roll_no:  # Check if the roll number matches
                print("\nStudent Found:")
                print(f"Roll No: {data[0]}")
                print(f"Name: {data[1]}")
                print(f"Division: {data[2]}")
                print(f"Address: {data[3]}")
                found = True
                break
    if not found:
        print("Student record not found!")

# Function to delete a student record
def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    found = False
    if not os.path.exists(FILENAME):  # Check if file exists
        print("No student records found.")
        return
    with open(FILENAME, "r") as file:
        lines = file.readlines()  # Read all lines into a list
    with open(FILENAME, "w") as file:
        for line in lines:
            if line.strip().split(",")[0] != roll_no:  # If the record does not match, keep it
                file.write(line)
            else:
                found = True  # Set flag to True if record is found
    if found:
        print("Student record deleted successfully!")
    else:
        print("Student record not found!")

# Main program loop
if __name__ == "__main__":
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()  # Add a new student
        elif choice == "2":
            display_student()  # Display student details
        elif choice == "3":
            delete_student()  # Delete a student record
        elif choice == "4":
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice, please try again!")  # Invalid input handling
