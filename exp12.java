import java.util.*;

public class SortingAlgorithms {
    
    // Heap Sort Implementation
    public static void heapSort(int[] arr) {
        int n = arr.length;
        
        // Build heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }
        
        // One by one extract elements from heap
        for (int i = n - 1; i > 0; i--) {
            // Swap the root (max element) with the last element
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Call heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }
    
    // To heapify a subtree rooted with node i which is an index in arr[]
    public static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }
        
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }
        
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            
            heapify(arr, n, largest);
        }
    }

    // Shell Sort Implementation
    public static void shellSort(int[] arr) {
        int n = arr.length;
        
        // Start with a large gap, then reduce the gap
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;
                
                // Shift earlier gap-sorted elements up until the correct location is found
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                
                // Put temp (the original arr[i]) in its correct location
                arr[j] = temp;
            }
        }
    }
    
    // Method to print an array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    // Main method to test the sorting algorithms
    public static void main(String[] args) {
        // Test data
        int[] arr1 = {12, 11, 13, 5, 6, 7};
        int[] arr2 = {12, 11, 13, 5, 6, 7};
        
        // Heap Sort Test
        System.out.println("Heap Sort:");
        System.out.println("Original Array:");
        printArray(arr1);
        heapSort(arr1);
        System.out.println("Sorted Array:");
        printArray(arr1);

        // Shell Sort Test
        System.out.println("\nShell Sort:");
        System.out.println("Original Array:");
        printArray(arr2);
        shellSort(arr2);
        System.out.println("Sorted Array:");
        printArray(arr2);
    }
}
