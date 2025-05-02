from collections import deque

# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: Represent a given graph using adjacency matrix/list to perform DFS and using adjacency list to perform BFS.
# Use the map of the area around the college as the graph. Identify the prominent landmarks as nodes and perform DFS and BFS on that.

# Landmarks around the college
landmarks = ["College", "Library", "Canteen", "Auditorium", "Playground", "Hostel"]

# Edges representing connections between landmarks (for example)
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]

# Adjacency Matrix Representation
matrix = [[0] * 6 for _ in range(6)]  # Initialize a 6x6 matrix with 0s
for u, v in edges:  # Set 1 for edges between landmarks
    matrix[u][v] = matrix[v][u] = 1

# Adjacency List Representation
adj = [[] for _ in range(6)]  # Initialize an empty adjacency list
for u, v in edges:  # Populate the adjacency list with neighbors
    adj[u].append(v)
    adj[v].append(u)

# DFS function using adjacency matrix
def dfs_matrix(v, vis):
    vis[v] = True  # Mark the current node as visited
    print(landmarks[v], end=" → ")  # Print the current node (landmark)
    for i in range(6):  # Traverse all neighbors of the current node
        if matrix[v][i] and not vis[i]:  # If there's an edge and the neighbor is not visited
            dfs_matrix(i, vis)  # Recursively visit the neighbor

# BFS function using adjacency list
def bfs_list(start):
    vis = [False] * 6  # Initialize the visited list
    q = deque([start])  # Use a queue for BFS
    vis[start] = True  # Mark the starting node as visited
    while q:
        v = q.popleft()  # Dequeue a node
        print(landmarks[v], end=" → ")  # Print the current node (landmark)
        for u in adj[v]:  # Traverse all neighbors of the current node
            if not vis[u]:  # If the neighbor is not visited
                vis[u] = True  # Mark the neighbor as visited
                q.append(u)  # Enqueue the neighbor

# --- MAIN ---
print("DFS Traversal (Adjacency Matrix):")
vis = [False] * 6  # Initialize the visited list for DFS
dfs_matrix(0, vis)  # Start DFS from the "College" (index 0)
print("\n")

print("BFS Traversal (Adjacency List):")
bfs_list(0)  # Start BFS from the "College" (index 0)
