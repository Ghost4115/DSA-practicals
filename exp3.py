#Name:Manav Mangesh Uttekar
#Roll no.: 71
#Problem statement: A book consists of chapters, chapters consist of
#sections and sections consist of subsections.Construct a tree and print
#the nodes. Find the time and space requirements of your method.


# Node class representing each element (book, chapter, section, subsection)
class TreeNode:
    def __init__(self, name):
        # Initialize the node with a name and an empty list of children
        self.name = name
        self.children = []

    def add_child(self, node):
        # Add a child node (e.g., a section or subsection) to the current node
        self.children.append(node)

    def print_tree(self, level=0):
        # Print the current node's name, with indentation based on its level in the tree
        print(" " * level + self.name)
        # Recursively print each child node, increasing the indentation for each level
        for child in self.children:
            child.print_tree(level + 1)

# Constructing the tree structure
book = TreeNode("Book")  # Root node representing the book

# Adding chapters
ch1 = TreeNode("Chapter 1")
ch2 = TreeNode("Chapter 2")
book.add_child(ch1)  # Adding Chapter 1 to the book
book.add_child(ch2)  # Adding Chapter 2 to the book

# Adding sections to Chapter 1
sec11 = TreeNode("Section 1.1")
sec12 = TreeNode("Section 1.2")
ch1.add_child(sec11)  # Adding Section 1.1 to Chapter 1
ch1.add_child(sec12)  # Adding Section 1.2 to Chapter 1

# Adding subsections to Section 1.1
subsec111 = TreeNode("Subsection 1.1.1")
subsec112 = TreeNode("Subsection 1.1.2")
sec11.add_child(subsec111)  # Adding Subsection 1.1.1 to Section 1.1
sec11.add_child(subsec112)  # Adding Subsection 1.1.2 to Section 1.1

# Adding sections to Chapter 2
sec21 = TreeNode("Section 2.1")
ch2.add_child(sec21)  # Adding Section 2.1 to Chapter 2

# Adding subsections to Section 2.1
sec21.add_child(TreeNode("Subsection 2.1.1"))  # Adding Subsection 2.1.1 to Section 2.1

# Printing the tree structure
book.print_tree()
