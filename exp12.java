import java.util.*;

public class SortingAlgorithms {

    // Heap Sort Implementation
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Build the max-heap (rearrange the array)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i); // Heapify each subtree starting from the last non-leaf node
        }

        // One by one extract elements from the heap
        for (int i = n - 1; i > 0; i--) {
            // Move current root (maximum) to the end of the array
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Call heapify on the reduced heap (heapify the root)
            heapify(arr, i, 0);
        }
    }

    // To heapify a subtree rooted with node i which is an index in arr[]
    public static void heapify(int[] arr, int n, int i) {
        int largest = i; // Initialize largest as root
        int left = 2 * i + 1; // left = 2*i + 1 (left child)
        int right = 2 * i + 2; // right = 2*i + 2 (right child)

        // If left child is larger than root
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        // If right child is larger than root
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        // If largest is not root, swap and heapify again
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify the affected subtree
            heapify(arr, n, largest);
        }
    }

    // Shell Sort Implementation
    public static void shellSort(int[] arr) {
        int n = arr.length;

        // Start with a large gap, then reduce the gap
        for (int gap = n / 2; gap > 0; gap /= 2) {
            // Perform a gapped insertion sort
            for (int i = gap; i < n; i++) {
                int temp = arr[i]; // Store the current element
                int j = i;

                // Shift earlier gap-sorted elements up until the correct location is found
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }

                // Place the temp element in its correct location
                arr[j] = temp;
            }
        }
    }

    // Method to print an array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " "); // Print each element followed by space
        }
        System.out.println(); // Move to the next line after printing the array
    }

    // Method to take input from the user
    public static int[] takeInput() {
        Scanner sc = new Scanner(System.in);

        // Prompt user for the number of elements in the array
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n]; // Declare an array of size n

        // Prompt user for the elements of the array
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt(); // Read each element into the array
        }

        return arr; // Return the array
    }

    // Main method to test the sorting algorithms
    public static void main(String[] args) {
        // Take user input for the array to be sorted
        int[] arr1 = takeInput();  // Array for Heap Sort
        int[] arr2 = Arrays.copyOf(arr1, arr1.length);  // Copy arr1 to arr2 for Shell Sort

        // Heap Sort Test
        System.out.println("Heap Sort:");
        System.out.println("Original Array:");
        printArray(arr1); // Print the original array
        heapSort(arr1);    // Apply Heap Sort
        System.out.println("Sorted Array:");
        printArray(arr1); // Print the sorted array

        // Shell Sort Test
        System.out.println("\nShell Sort:");
        System.out.println("Original Array:");
        printArray(arr2); // Print the original array
        shellSort(arr2);   // Apply Shell Sort
        System.out.println("Sorted Array:");
        printArray(arr2); // Print the sorted array
    }
}
