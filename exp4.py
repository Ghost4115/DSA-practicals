#Name:Manav Mangesh Uttekar
#Roll no.: 71
#Problem statement: Construct an expression tree from the given prefix
#expression eg. +-a*bc/def and traverse it using post order traversal (non
#recursive) and then delete the entire tree.



class Node:
    def __init__(self, data):
        self.data = data  # Stores the node data (operator/operand)
        self.left = None   # Left child of the node
        self.right = None  # Right child of the node

# Step 1: Construct Expression Tree from Prefix
def is_operator(c):
    return c in '+*/-'  # Check if the character is an operator

def construct_tree(prefix):
    stack = []  # Stack to hold nodes while building the tree
    # Traverse the prefix expression from right to left
    for ch in reversed(prefix):
        node = Node(ch)  # Create a new node for the character
        if is_operator(ch):  # If it's an operator, pop two nodes and make them children
            node.left = stack.pop()  # Left child
            node.right = stack.pop()  # Right child
        stack.append(node)  # Push the node onto the stack
    return stack[-1]  # The root of the tree will be the last element in the stack

# Step 2: Postorder Traversal (Non-Recursive)
def postorder_non_recursive(root):
    if not root:
        return
    stack1, stack2 = [root], []  # stack1 is for traversal, stack2 holds the postorder result
    while stack1:
        node = stack1.pop()  # Pop a node from stack1
        stack2.append(node)  # Push it onto stack2 (this will give postorder)
        if node.left:
            stack1.append(node.left)  # Add left child to stack1
        if node.right:
            stack1.append(node.right)  # Add right child to stack1
    # Print the contents of stack2, which contains nodes in postorder
    while stack2:
        print(stack2.pop().data, end=' ')

# Step 3: Delete Tree
def delete_tree(root):
    if not root:
        return
    stack = [root]  # Stack to traverse the tree and delete nodes
    while stack:
        node = stack.pop()  # Pop a node from the stack
        if node.right:
            stack.append(node.right)  # Add right child to stack
        if node.left:
            stack.append(node.left)  # Add left child to stack
        node.left = node.right = None  # Clear references to children
        del node  # Delete the node to free memory

# --- Main ---
prefix = "+-a*bc/def"  # Prefix expression
root = construct_tree(prefix)  # Construct the tree from the prefix expression

print("Postorder (non-recursive):")
postorder_non_recursive(root)  # Perform non-recursive postorder traversal
print()

# Delete the entire tree
delete_tree(root)
