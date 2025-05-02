# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: Beginning with an empty binary search tree, construct a binary search tree by inserting the values in the order given. After constructing the binary tree:
# i. Insert a new node
# ii. Find the number of nodes in the longest path from root
# iii. Find the minimum data value in the tree
# iv. Change the tree so that the roles of the left and right pointers are swapped at every node
# v. Search for a value in the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 1. Insert into BST
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# 2. Height of tree (longest path)
def longest_path(root):
    if not root:
        return 0
    return 1 + max(longest_path(root.left), longest_path(root.right))

# 3. Minimum value in BST
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.data

# 4. Mirror the tree
def mirror(root):
    if root:
        root.left, root.right = mirror(root.right), mirror(root.left)
    return root

# 5. Search in BST
def search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    return search(root.left, key) if key < root.data else search(root.right, key)

# Inorder Traversal for display
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# --- MAIN ---
# Taking input from the user
n = int(input("Enter the number of elements to insert in the BST: "))
values = [int(input(f"Enter value {i+1}: ")) for i in range(n)]

root = None
for val in values:
    root = insert(root, val)

print("\nInorder traversal of BST:")
inorder(root)

# Insert a new node (Taking input from the user)
new_value = int(input("\nEnter a value to insert into the BST: "))
root = insert(root, new_value)
print("\nAfter inserting the new value:")
inorder(root)

# Longest path from root
print("\n\nLongest path (height):", longest_path(root))

# Minimum data value
print("Minimum value in BST:", find_min(root))

# Mirror the tree
root = mirror(root)
print("\nInorder after mirroring:")
inorder(root)

# Search for a value (Taking input from the user)
search_key = int(input("\nEnter a value to search in the BST: "))
print(f"\nSearch for {search_key}: {'Found' if search(root, search_key) else 'Not found'}")
