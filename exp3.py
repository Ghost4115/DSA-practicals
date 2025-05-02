# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: A book consists of chapters, chapters consist of sections and sections consist of subsections.
# Construct a tree and print the nodes. Find the time and space requirements of your method.

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def print_tree(self, level=0):
        print(" " * level + self.name)
        for child in self.children:
            child.print_tree(level + 1)

# Constructing the tree
book = TreeNode("Book")
# Adding chapters
ch1 = TreeNode("Chapter 1")
ch2 = TreeNode("Chapter 2")
book.add_child(ch1)
book.add_child(ch2)

# Adding sections to Chapter 1
sec11 = TreeNode("Section 1.1")
sec12 = TreeNode("Section 1.2")
ch1.add_child(sec11)
ch1.add_child(sec12)

# Adding subsections to Section 1.1
subsec111 = TreeNode("Subsection 1.1.1")
subsec112 = TreeNode("Subsection 1.1.2")
sec11.add_child(subsec111)
sec11.add_child(subsec112)

# Adding sections to Chapter 2
sec21 = TreeNode("Section 2.1")
ch2.add_child(sec21)

# Adding subsections to Section 2.1
sec21.add_child(TreeNode("Subsection 2.1.1"))

# Print the tree
book.print_tree()
