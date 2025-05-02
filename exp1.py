# Name: Manav Mangesh Uttekar
# Roll no.: SE-71
# Problem statement: Consider telephone book database of N clients. Make
# use of a hash table implementation to quickly look up client‘s telephone
# number. Make use of two collision handling techniques (Chaining and Linear Probing)
# and compare them using the number of comparisons required to find a set of telephone numbers.

def simple_hash(key, size):
    # A simple hash function that calculates the hash value for a key based on its characters' ASCII sum
    return sum(ord(c) for c in key) % size

class HashTableChaining:
    # Implements a hash table using chaining to handle collisions.
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.table = [[] for _ in range(size)]  # Initialize an empty table with lists for chaining
        self.comparisons = 0  # To keep track of the number of comparisons during searches and insertions

    def insert(self, key, value):
        # Insert a key-value pair into the hash table using chaining.
        index = simple_hash(key, self.size)
        for i in range(len(self.table[index])):  # Traverse the chain at the computed index
            self.comparisons += 1  # Count a comparison for each element in the chain
            if self.table[index][i][0] == key:  # If key already exists, update the value
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))  # If key does not exist, append the new key-value pair

    def search(self, key):
        # Search for a key in the hash table using chaining
        index = simple_hash(key, self.size)
        for k, v in self.table[index]:  # Traverse the chain at the computed index
            self.comparisons += 1  # Count a comparison for each element in the chain
            if k == key:
                return v  # Return the value if the key is found
        return None  # Return None if the key is not found

class HashTableLinearProbing:
    # Implements a hash table using linear probing to handle collisions.
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.table = [None] * size  # Initialize an empty table with None values for probing
        self.comparisons = 0  # To keep track of the number of comparisons during searches and insertions

    def insert(self, key, value):
        # Insert a key-value pair into the hash table using linear probing.
        index = simple_hash(key, self.size)
        start_index = index  # Store the starting index to prevent infinite loops
        while self.table[index] is not None:  # Probe until an empty slot is found
            self.comparisons += 1  # Count a comparison for each probe
            if self.table[index][0] == key:  # If key already exists, break
                break
            index = (index + 1) % self.size  # Linear probe to the next slot
            if index == start_index:  # If we've circled back to the start, the table is full
                print("Error: Hash table full")
                return
        self.table[index] = (key, value)  # Insert the key-value pair at the found index

    def search(self, key):
        # Search for a key in the hash table using linear probing
        index = simple_hash(key, self.size)
        start_index = index  # Store the starting index to prevent infinite loops
        while self.table[index] is not None:  # Probe until an empty slot is found
            self.comparisons += 1  # Count a comparison for each probe
            if self.table[index][0] == key:  # If key is found, return its value
                return self.table[index][1]
            index = (index + 1) % self.size  # Linear probe to the next slot
            if index == start_index:  # If we've circled back to the start, the key is not in the table
                break
        return None  # Return None if the key is not found

def main():
    print("=== Telephone Book using Hash Tables ===")
    n = int(input("Enter number of clients: "))
    chaining = HashTableChaining(size=n)  # Create a hash table with chaining for collision handling
    probing = HashTableLinearProbing(size=2 * n)  # Create a hash table with linear probing for collision handling

    # Insert clients and their telephone numbers into both hash tables
    for i in range(n):
        name = input(f"Enter name of client {i+1}: ")
        number = input(f"Enter telephone number of {name}: ")
        chaining.insert(name, number)  # Insert into chaining-based hash table
        probing.insert(name, number)   # Insert into linear probing-based hash table

    m = int(input("\nEnter number of clients to search: "))
    to_search = []
    for i in range(m):
        name = input(f"Enter name to search ({i+1}): ")
        to_search.append(name)

    print("\n=== Search Results ===")
    # Search for each client in both hash tables and print the results
    for name in to_search:
        ch_result = chaining.search(name)
        lp_result = probing.search(name)
        print(f"{name}:")
        if ch_result is not None:
            print(f" Chaining Result: {ch_result}")
        else:
            print(" Chaining Result: Not found")
        if lp_result is not None:
            print(f" Linear Probing Result: {lp_result}")
        else:
            print(" Linear Probing Result: Not found")

    print("\n=== Comparisons Count ===")
    # Print the number of comparisons made during search operations for both methods
    print("Chaining comparisons:", chaining.comparisons)
    print("Linear Probing comparisons:", probing.comparisons)

if __name__ == "__main__":
    main()
