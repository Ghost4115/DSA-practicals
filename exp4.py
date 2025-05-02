# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: Construct an expression tree from the given prefix expression eg. +-a*bc/def and traverse it using post order traversal (non recursive) and then delete the entire tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Step 1: Construct Expression Tree from Prefix
def is_operator(c):
    return c in '+*/'

def construct_tree(prefix):
    stack = []
    for ch in reversed(prefix):
        node = Node(ch)
        if is_operator(ch):
            node.left = stack.pop()
            node.right = stack.pop()
        stack.append(node)
    return stack[-1]

# Step 2: Postorder Traversal (Non-Recursive)
def postorder_non_recursive(root):
    if not root:
        return
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().data, end=' ')

# Step 3: Delete Tree
def delete_tree(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node.left = node.right = None  # Remove references
        del node

# --- Main ---
prefix = "+-a*bc/def"
root = construct_tree(prefix)

print("Postorder (non-recursive):")
postorder_non_recursive(root)
print()

# Delete tree
delete_tree(root)
