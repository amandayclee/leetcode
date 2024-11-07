class ArrayMatrixManipulationPractice:

    # Exercise 1: Sum of Array Elements
    # Given an array of integers, find and return the sum of all elements.
    @staticmethod
    def sum_array(arr):
        # TODO: Fill in the logic
        cur_sum = 0
        for num in arr:
            cur_sum += num
        return cur_sum
    
    def sum_array_recursive(arr):
        if not arr:
            return 0
        return arr[0] + ArrayMatrixManipulationPractice.sum_array_recursive(arr[1:])

    # Exercise 2: Maximum Element in Array
    # Given an array of integers, find and return the maximum element.
    @staticmethod
    def max_element(arr):
        # TODO: Fill in the logic
        if not arr:
            return None
        
        max_num = float('-inf')
        for num in arr:
            max_num = max(num, max_num)
        
        return max_num
    
    def max_elemenet_recursive(arr):
        if not arr:
            return None
        
        if len(arr) == 1:
            return arr[0]
        
        rest_max = ArrayMatrixManipulationPractice.max_elemenet_recursive(arr[1:])
        return arr[0] if arr[0] > rest_max else rest_max

    # Exercise 3: Reverse an Array
    # Given an array of integers, reverse the array and return it.
    @staticmethod
    def reverse_array(arr):
        # TODO: Fill in the logic
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr

    # Exercise 4: Left Rotation of Array
    # Given an array, rotate the array to the left by 1 position.
    @staticmethod
    def rotate_left(arr):
        # TODO: Fill in the logic
        first_ele = arr[0]
        for i in range(0, len(arr) - 1):
            arr[i] = arr[i + 1]
        
        arr[-1] = first_ele
        
        return arr
    
    def rotate_left_cyclic(arr):
        if len(arr) <= 1:
            return arr
            
        n = len(arr)
        temp = arr[0]
        idx = 0
        
        for _ in range(n):
            next_idx = (idx + 1) % n
            next_temp = arr[next_idx]
            arr[next_idx] = temp
            temp = next_temp
            idx = next_idx
            
        return arr

    # Exercise 5: Right Rotation of Array
    # Given an array, rotate the array to the right by 1 position.
    @staticmethod
    def rotate_right(arr):
        # TODO: Fill in the logic
        last_ele = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
            
        arr[0] = last_ele
        
        return arr
    
    def rotate_right_cyclic(arr):
        if len(arr) <= 1:
            return arr
        
        n = len(arr)
        temp = arr[-1] 
        idx = n - 1 
        
        for _ in range(n):
            next_idx = (idx - 1) % n
            next_temp = arr[next_idx]
            arr[next_idx] = temp
            temp = next_temp
            idx = next_idx
            
        return arr
            

    # Exercise 6: 2D Array Diagonal Sum
    # Given a square matrix, find and return the sum of the elements along both diagonals.
    @staticmethod
    def diagonal_sum(matrix):
        # TODO: Fill in the logic
        return 0

    # Exercise 7: Spiral Matrix Printing
    # Given a 2D matrix, print its elements in spiral order.
    @staticmethod
    def print_spiral_matrix(matrix):
        # TODO: Fill in the logic

    # Exercise 8: Transpose of a Matrix
    # Given a 2D matrix, return its transpose.
    @staticmethod
    def transpose_matrix(matrix):
        # TODO: Fill in the logic
        return matrix

    # Exercise 9: Row-wise Maximum of Matrix
    # Given a 2D matrix, return the maximum element of each row.
    @staticmethod
    def row_wise_max(matrix):
        # TODO: Fill in the logic
        return []

    # Exercise 10: Column-wise Minimum of Matrix
    # Given a 2D matrix, return the minimum element of each column.
    @staticmethod
    def column_wise_min(matrix):
        # TODO: Fill in the logic
        return []

    # Exercise 11: Sum of Each Row and Column
    # Given a 2D matrix, return the sum of each row and each column separately.
    @staticmethod
    def row_column_sums(matrix):
        # TODO: Fill in the logic

    # Exercise 12: Check Symmetric Matrix
    # Given a square matrix, check whether it is symmetric (i.e., equal to its transpose).
    @staticmethod
    def is_symmetric(matrix):
        # TODO: Fill in the logic
        return False

    # Exercise 13: Matrix Multiplication
    # Given two matrices, perform matrix multiplication and return the result.
    @staticmethod
    def matrix_multiplication(matrix_a, matrix_b):
        # TODO: Fill in the logic
        return []

    # Exercise 14: Find Duplicates in Array
    # Given an array, return all the duplicate elements.
    @staticmethod
    def find_duplicates(arr):
        # TODO: Fill in the logic
        return []

    # Exercise 15: Find Missing Element in Array
    # Given an array of n-1 integers, find the missing number in the range from 1 to n.
    @staticmethod
    def find_missing_element(arr, n):
        # TODO: Fill in the logic
        return 0

    # Exercise 16: Array Prefix Sum
    # Given an array of integers, return the prefix sum array.
    @staticmethod
    def prefix_sum(arr):
        # TODO: Fill in the logic
        return arr

    # Exercise 17: Check if Array is Sorted
    # Given an array, check whether the array is sorted in non-decreasing order.
    @staticmethod
    def is_sorted(arr):
        # TODO: Fill in the logic
        return False

    # Exercise 18: Find Pair with Given Sum
    # Given an array and a target sum, find a pair of elements whose sum equals the target.
    @staticmethod
    def find_pair_with_sum(arr, target):
        # TODO: Fill in the logic
        return []

    # Exercise 19: Merge Two Sorted Arrays
    # Given two sorted arrays, merge them into a single sorted array.
    @staticmethod
    def merge_sorted_arrays(arr1, arr2):
        # TODO: Fill in the logic
        return []

    # Exercise 20: Find Majority Element
    # Given an array, find the element that appears more than n/2 times. Return -1 if no such element exists.
    @staticmethod
    def find_majority_element(arr):
        # TODO: Fill in the logic
        return -1


# Test cases with assertions
def run_tests():
    practice = ArrayMatrixManipulationPractice()

    # Test sumArray
    assert practice.sum_array([1, 2, 3, 4]) == 10, "Test failed for sum_array"
    
    # Test maxElement
    assert practice.max_element([1, 7, 3, 9, 5]) == 9, "Test failed for max_element"
    
    # Test reverseArray
    assert practice.reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1], "Test failed for reverse_array"
    
    # Test rotateLeft
    assert practice.rotate_left([1, 2, 3, 4]) == [2, 3, 4, 1], "Test failed for rotate_left"
    
    # Test rotateRight
    assert practice.rotate_right([1, 2, 3, 4]) == [4, 1, 2, 3], "Test failed for rotate_right"
    
    # Test diagonalSum
    assert practice.diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25, "Test failed for diagonal_sum"
    
    # Test printSpiralMatrix - no assertion as it's a print function
    
    # Test transposeMatrix
    assert practice.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Test failed for transpose_matrix"
    
    # Test rowWiseMax
    assert practice.row_wise_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [3, 6, 9], "Test failed for row_wise_max"
    
    # Test columnWiseMin
    assert practice.column_wise_min([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3], "Test failed for column_wise_min"
    
    # Test rowColumnSums - no assertion as it's a print function
    
    # Test isSymmetric
    assert practice.is_symmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]) == True, "Test failed for is_symmetric"
    
    # Test matrixMultiplication
    assert practice.matrix_multiplication([[1, 2], [3, 4]], [[2, 0], [1, 2]]) == [[4, 4], [10, 8]], "Test failed for matrix_multiplication"
    
    # Test findDuplicates
    assert practice.find_duplicates([1, 2, 2, 3, 4, 4, 5]) == [2, 4], "Test failed for find_duplicates"
    
    # Test findMissingElement
    assert practice.find_missing_element([1, 2, 3, 5], 5) == 4, "Test failed for find_missing_element"
    
    # Test prefixSum
    assert practice.prefix_sum([1, 2, 3, 4]) == [1, 3, 6, 10], "Test failed for prefix_sum"
    
    # Test isSorted
    assert practice.is_sorted([1, 2, 3, 4]) == True, "Test failed for is_sorted"
    
    # Test findPairWithSum
    assert practice.find_pair_with_sum([1, 2, 3, 4], 5) == [(1, 4)], "Test failed for find_pair_with_sum"
    
    # Test mergeSortedArrays
    assert practice.merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6], "Test failed for merge_sorted_arrays"
    
    # Test findMajorityElement
    assert practice.find_majority_element([1, 2, 2, 2, 3]) == 2, "Test failed for find_majority_element"
    
    print("All tests passed!")


# Call run_tests to test all functions
run_tests()