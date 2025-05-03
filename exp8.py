#Name: Manav Uttekar
#Rollno:71
#Problem Statement: Given sequence k = k1 <k2 < … <kn of n sorted keys,
#with a search probability pi for each key
#ki . Build the Binary search tree that has the least search cost given
#the access probability for each
#key?

import sys

# Function to calculate the minimum search cost for an optimal BST
def optimal_bst(keys, freq, n):
    # Create a 2D table to store the cost of the optimal BST
    cost = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill in the cost table for individual keys (length 1 subproblems)
    for i in range(n):
        cost[i][i] = freq[i]
    
    # L is the chain length, ranging from 2 to n
    for L in range(2, n + 1):  # L is the chain length
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = sys.maxsize  # Initialize with a large value
            
            # Try making all keys in the interval keys[i..j] as the root
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    sum(freq[i:j + 1])  # Sum of probabilities in this range
                
                if c < cost[i][j]:
                    cost[i][j] = c
    
    # The result is stored in cost[0][n-1]
    return cost[0][n - 1]

# Main function to take input and call the optimal_bst function
def main():
    n = int(input("Enter number of elements: "))  # Number of keys
    keys = list(map(int, input("Enter keys (sorted): ").split()))  # Sorted keys
    freq = list(map(float, input("Enter search probabilities: ").split()))  # Search probabilities for each key
    
    # Check if the number of keys and probabilities match the specified count
    if len(keys) != n or len(freq) != n:
        print("Error: Number of keys and probabilities must match the specified count.")
        return
    
    # Calculate the minimum cost of the optimal BST
    min_cost = optimal_bst(keys, freq, n)
    
    # Output the minimum cost
    print(f"Optimal BST cost: {min_cost}")

# Run the main function when this script is executed
if __name__ == "__main__":
    main()
