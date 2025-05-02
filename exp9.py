# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: A Dictionary stores keywords and its meanings.
# Provide facility for adding new keywords, deleting keywords, updating
# values of any entry. Provide facility to display whole data sorted in
# ascending/descending order. Also find how many maximum comparisons 
# may be required for finding any keyword. Use Height-balanced tree (AVL Tree)
# and find the complexity for finding a keyword.

class Node:
    def __init__(self, key, meaning):
        self.key = key          # Keyword
        self.meaning = meaning  # Meaning of the keyword
        self.left = None        # Left child pointer
        self.right = None       # Right child pointer
        self.height = 1         # Height of the node, initially 1

class AVLTreeDict:
    
    # Insert a new node into the AVL tree
    def insert(self, root, key, meaning):
        if not root:
            return Node(key, meaning)
        
        # Insert in left or right subtree based on the key comparison
        if key < root.key:
            root.left = self.insert(root.left, key, meaning)
        elif key > root.key:
            root.right = self.insert(root.right, key, meaning)
        else:
            print("Key already exists.")  # No duplicate keys allowed
            return root
        
        # Update the height of the current node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # Balance the tree if needed
        balance = self.getBalance(root)
        
        # Left heavy case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        
        # Right heavy case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        
        # Left-right case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Right-left case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    # Delete a node from the AVL tree
    def delete(self, root, key):
        if not root:
            return root
        
        # Perform standard BST deletion
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children
            temp = self.getMinValueNode(root.right)
            root.key, root.meaning = temp.key, temp.meaning
            root.right = self.delete(root.right, temp.key)
        
        # Update the height of the current node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # Balance the tree if needed
        balance = self.getBalance(root)
        
        # Left heavy case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        
        # Right heavy case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        
        # Left-right case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Right-left case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    # Update meaning of an existing keyword
    def update(self, root, key, new_meaning):
        node, cmp = self.search(root, key)
        if node:
            node.meaning = new_meaning
            print(f"Updated '{key}' with new meaning.")
        else:
            print("Key not found.")
    
    # Search for a keyword in the AVL tree
    def search(self, root, key):
        count = 0
        while root:
            count += 1
            if key == root.key:
                print(f"Found '{key}' in {count} comparisons.")
                return root, count
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        print("Key not found.")
        return None, count

    # In-order traversal to display data in ascending order
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(f"{root.key}: {root.meaning}")
            self.inOrder(root.right)

    # Reverse in-order traversal to display data in descending order
    def reverseOrder(self, root):
        if root:
            self.reverseOrder(root.right)
            print(f"{root.key}: {root.meaning}")
            self.reverseOrder(root.left)

    # Get the height of the node
    def getHeight(self, root):
        return root.height if root else 0

    # Get the balance factor of the node
    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    # Left rotation for balancing
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Right rotation for balancing
    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    # Get the minimum value node in the tree
    def getMinValueNode(self, node):
        while node.left:
            node = node.left
        return node


# ---- Demo ----
if __name__ == "__main__":
    tree = AVLTreeDict()
    root = None
    while True:
        print("\n1. Add 2. Delete 3. Update 4. Display Asc 5. Desc 6. Search 7. Exit")
        ch = int(input("Enter choice: "))
        
        if ch == 1:
            k = input("Enter keyword: ")
            m = input("Enter meaning: ")
            root = tree.insert(root, k, m)
        elif ch == 2:
            k = input("Enter keyword to delete: ")
            root = tree.delete(root, k)
        elif ch == 3:
            k = input("Enter keyword to update: ")
            m = input("Enter new meaning: ")
            tree.update(root, k, m)
        elif ch == 4:
            print("Ascending order:")
            tree.inOrder(root)
        elif ch == 5:
            print("Descending order:")
            tree.reverseOrder(root)
        elif ch == 6:
            k = input("Enter keyword to search: ")
            _, cmp = tree.search(root, k)
        else:
            break
