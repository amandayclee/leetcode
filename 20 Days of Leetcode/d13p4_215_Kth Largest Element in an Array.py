from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.buildMinHeap(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                self.delete(heap)
                self.insert(heap, num)
        return heap[0]
        
    def buildMinHeap(self, arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def heapify(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

    def insert(self, arr, key):
        arr.append(key)
        n = len(arr)
        i = n - 1
        while i > 0 and arr[i] < arr[(i - 1) // 2]:
            arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            i = (i - 1) // 2

    def delete(self, arr):
        n = len(arr)
        if n == 0:
            return None
        root = arr[0]
        arr[0] = arr[n - 1]
        arr.pop()
        self.heapify(arr, n - 1, 0)
        return root

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([[7,6,5,4,3,2,1], 5]), "expected_output": 3}
    ]
    for test_case in test_cases:
        assert solution.findKthLargest(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]
