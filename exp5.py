# Define a Node class for the binary search tree (BST)
class Node:
    def __init__(self, data):
        self.data = data  # Data for the node (value of the node)
        self.left = None   # Left child of the node
        self.right = None  # Right child of the node

# 1. Insert function: Inserts a new node in the BST following the BST property
def insert(root, key):
    if not root:
        # If the root is None, create a new node with the given key
        return Node(key)
    
    # If key is smaller, it should go to the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        # If key is larger, it should go to the right subtree
        root.right = insert(root.right, key)
    
    return root  # Return the root (after insertion)

# 2. Function to calculate the height of the tree (Longest path from root)
def longest_path(root):
    if not root:
        # If the root is None, the height is 0
        return 0
    
    # Calculate the height of both subtrees and add 1 for the current node
    return 1 + max(longest_path(root.left), longest_path(root.right))

# 3. Function to find the minimum value in the BST
def find_min(root):
    current = root
    # Loop down to find the leftmost leaf (minimum value)
    while current.left:
        current = current.left
    return current.data  # Return the minimum value

# 4. Function to mirror the tree: Swap left and right pointers at every node
def mirror(root):
    if root:
        # Swap left and right children of the node
        root.left, root.right = mirror(root.right), mirror(root.left)
    return root  # Return the root of the mirrored tree

# 5. Function to search for a value in the BST
def search(root, key):
    if not root:
        # If root is None, the key is not found
        return False
    
    if root.data == key:
        # If key matches the root's data, return True
        return True
    
    # If key is smaller, search in the left subtree
    if key < root.data:
        return search(root.left, key)
    # If key is larger, search in the right subtree
    else:
        return search(root.right, key)

# Function for Inorder Traversal (for displaying the tree in sorted order)
def inorder(root):
    if root:
        inorder(root.left)   # Traverse left subtree
        print(root.data, end=' ')  # Print current node's data
        inorder(root.right)  # Traverse right subtree

# --- MAIN --- 
# Taking input from the user for BST construction
n = int(input("Enter the number of elements to insert in the BST: "))
values = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

root = None
# Insert each value into the BST
for val in values:
    root = insert(root, val)

# Print the Inorder traversal of the BST (This gives the nodes in sorted order)
print("\nInorder traversal of BST:")
inorder(root)

# Insert a new node (Taking input from the user)
new_value = int(input("\nEnter a value to insert into the BST: "))
root = insert(root, new_value)
print("\nAfter inserting the new value:")
inorder(root)  # Display the BST after insertion

# Find the longest path (height of the tree)
print("\n\nLongest path (height):", longest_path(root))

# Find the minimum data value in the BST
print("Minimum value in BST:", find_min(root))

# Mirror the tree (swap left and right pointers)
root = mirror(root)
print("\nInorder after mirroring:")
inorder(root)  # Display the tree after mirroring

# Search for a value in the BST (Taking input from the user)
search_key = int(input("\nEnter a value to search in the BST: "))
# Search the tree and print whether the value is found
print(f"\nSearch for {search_key}: {'Found' if search(root, search_key) else 'Not found'}")
