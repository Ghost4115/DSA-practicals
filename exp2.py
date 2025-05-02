# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: Implement all the functions of a dictionary (ADT) using hashing and handle collisions using chaining with/without replacement.
# Data: Set of (key, value) pairs, Keys are mapped to values, Keys must be comparable, Keys must be unique.
# Standard Operations: Insert(key, value), Find(key), Delete(key)

# A simple hash function to compute an index from the key. It sums up the ASCII values of each character 
# in the key and returns the remainder when divided by the table size (hashing).
def simple_hash(key, size):
    return sum(ord(c) for c in key) % size

class Dictionary:
    def __init__(self, size, mode="with"):
        # Initialize the dictionary with the given table size and mode (collision handling).
        self.size = size
        self.mode = mode  # "with" for replacement, "without" for ignoring duplicate keys
        self.table = [[] for _ in range(size)]  # Create a table (list of lists) for chaining collisions

    def insert(self, key, value):
        # Insert a (key, value) pair into the hash table.
        index = simple_hash(key, self.size)  # Calculate the index for the key using the hash function
        for i in range(len(self.table[index])):  # Check if key already exists at this index
            if self.table[index][i][0] == key:  # Key found
                if self.mode == "with":  # If "with" mode, update the value
                    self.table[index][i] = (key, value)
                    print(f"Updated key '{key}' with new value.")
                    return
                else:  # If "without" mode, skip insertion to avoid duplicates
                    print(f"Key '{key}' already exists. Skipping insert (without replacement).")
                    return
        self.table[index].append((key, value))  # Insert new key-value pair at the calculated index
        print(f"Inserted key '{key}' successfully.")

    def find(self, key):
        # Find and return the value for the given key.
        index = simple_hash(key, self.size)  # Calculate the index using the hash function
        for k, v in self.table[index]:  # Traverse the chain at the given index
            if k == key:  # If the key is found, return the associated value
                print(f"Found: {key} => {v}")
                return v
        print(f"Key '{key}' not found.")  # If key is not found in the chain
        return None

    def delete(self, key):
        # Delete a (key, value) pair from the hash table.
        index = simple_hash(key, self.size)  # Calculate the index for the key using the hash function
        for i in range(len(self.table[index])):  # Traverse the chain at the given index
            if self.table[index][i][0] == key:  # If the key is found, remove it
                del self.table[index][i]
                print(f"Deleted key '{key}'.")
                return True
        print(f"Key '{key}' not found for deletion.")  # If key is not found
        return False

    def display(self):
        # Display the current state of the dictionary (the entire hash table with its chains).
        print("\nCurrent state of the dictionary:")
        for i in range(self.size):
            if self.table[i]:  # If there are key-value pairs at this index, display them
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: Empty")  # If the index is empty
        print()

def main():
    # Main function to interact with the user, allowing them to insert, find, delete, and display the dictionary.
    print("=== Dictionary ADT using Hashing with Chaining ===")
    size = int(input("Enter size of the hash table: "))  # Ask the user for the table size
    print("\nChoose collision handling mode:")
    print("1. With replacement (updates existing keys)")  # Mode to handle collisions with replacement
    print("2. Without replacement (ignores duplicate keys)")  # Mode to handle collisions without replacement
    mode_choice = input("Enter 1 or 2: ")
    if mode_choice == "1":
        mode = "with"  # Set mode to "with" if user selects 1
    elif mode_choice == "2":
        mode = "without"  # Set mode to "without" if user selects 2
    else:
        print("Invalid choice. Defaulting to 'with replacement'.")  # Default to "with" if input is invalid
        mode = "with"

    d = Dictionary(size, mode)  # Create a dictionary instance with the given size and mode

    while True:
        # Provide the user with options to interact with the dictionary
        print("\nOptions:")
        print("1. Insert (key, value)")
        print("2. Find (key)")
        print("3. Delete (key)")
        print("4. Display Dictionary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            key = input("Enter key: ")  # Ask for the key to insert
            value = input("Enter value: ")  # Ask for the value to insert
            d.insert(key, value)  # Call insert method
        elif choice == "2":
            key = input("Enter key to find: ")  # Ask for the key to find
            d.find(key)  # Call find method
        elif choice == "3":
            key = input("Enter key to delete: ")  # Ask for the key to delete
            d.delete(key)  # Call delete method
        elif choice == "4":
            d.display()  # Display the current dictionary state
        elif choice == "5":
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice. Try again.")  # Handle invalid choices

if __name__ == "__main__":
    main()  # Run the main function to start the program

