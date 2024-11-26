from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # nums[mid] < nums[left]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([4,5,6,7,0,1,2], 0), "expected_output": 4},
        {"input": ([4,5,6,7,0,1,2], 3), "expected_output": -1},
        {"input": ([1], 0), "expected_output": -1}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        result = solution.search(*input_data)
        assert abs(result - expected_output) < 1e-5, f"Test case failed: {test_case}, got {result} instead of {expected_output}"
    
    print("All test cases passed!")
        