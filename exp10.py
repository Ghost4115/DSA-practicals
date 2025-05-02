# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: Read the marks obtained by students of second year 
# in an online examination of a particular subject. Find out maximum 
# and minimum marks obtained in that subject. Use heap data structure.
# Analyze the algorithm.

import heapq

def find_min_max_marks(marks):
    # Create a min-heap and max-heap
    min_heap = []
    max_heap = []

    # Insert all marks into both heaps
    for mark in marks:
        heapq.heappush(min_heap, mark)  # Min-heap (default behavior of heapq)
        heapq.heappush(max_heap, -mark)  # Max-heap (invert the sign to use min-heap as max-heap)

    # The minimum mark will be the root of the min-heap
    min_mark = min_heap[0]

    # The maximum mark will be the root of the max-heap
    max_mark = -max_heap[0]

    return min_mark, max_mark

# Taking input from the user
num_students = int(input("Enter the number of students: "))
marks = []

# Getting marks of students from the user
for i in range(num_students):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

# Find the minimum and maximum marks
min_mark, max_mark = find_min_max_marks(marks)

# Output the results
print(f"Minimum mark: {min_mark}")
print(f"Maximum mark: {max_mark}")
