from collections import defaultdict, deque

# Name: Manav Mangesh Uttekar
# Roll no.: 71
# Problem statement: There are flight paths between cities. If there is a flight between city A and city B, then there is an edge between the cities.
# The cost of the edge can be the time that the flight takes to reach city B from A, or the amount of fuel used for the journey.
# Represent this as a graph. The node can be represented by airport name or the name of the city. 
# Use adjacency list or adjacency matrix representation of the graph. Check whether the graph is connected or not.
# Justify the storage representation used.

# Define a class for Flight Graph
class FlightGraph:
    def __init__(self):
        # Adjacency list representation: Each city has a list of tuples (neighboring city, flight time)
        self.adj = defaultdict(list)  # City -> list of (neighbor, time)
        
    # Add a flight between two cities with a given time (undirected graph)
    def add_flight(self, city_from, city_to, time):
        self.adj[city_from].append((city_to, time))  # Add the flight from city_from to city_to
        self.adj[city_to].append((city_from, time))  # Add the flight from city_to to city_from (undirected graph)
        
    # Display the adjacency list representation of the graph
    def display(self):
        print("Adjacency List Representation of Flight Graph:")
        for city in self.adj:
            # Format the connections for each city
            connections = ', '.join([f"({dest}, time={time})" for dest, time in self.adj[city]])
            print(f"{city} -> {connections}")
    
    # Check if the graph is connected using BFS or DFS
    def is_connected(self):
        if not self.adj:
            return True  # If there are no cities, we assume the graph is trivially connected
            
        visited = set()  # To track visited cities
        queue = deque()  # BFS queue
        start = next(iter(self.adj))  # Start from any city (choose the first one)
        queue.append(start)
        visited.add(start)
        
        while queue:
            current = queue.popleft()  # Dequeue a city
            for neighbor, _ in self.adj[current]:
                if neighbor not in visited:  # If not visited, mark it as visited
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        # If the number of visited cities equals the total number of cities, the graph is connected
        return len(visited) == len(self.adj)

# Example usage
graph = FlightGraph()

# Add flights (edges) between cities
graph.add_flight("Mumbai", "Delhi", 120)
graph.add_flight("Delhi", "Bangalore", 180)
graph.add_flight("Mumbai", "Chennai", 150)
graph.add_flight("Chennai", "Kolkata", 200)

# Display the graph
graph.display()

# Check if the flight graph is connected
if graph.is_connected():
    print("\nThe flight graph is CONNECTED.")
else:
    print("\nThe flight graph is NOT connected.")
