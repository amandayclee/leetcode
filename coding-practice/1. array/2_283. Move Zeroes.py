# https://leetcode.com/problems/move-zeroes/description/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_zero_at = 0 # use to move all non-zero values to the left side
        
        for check_every_element_at in range(len(nums)):
            if nums[check_every_element_at] != 0:
                nums[start_zero_at] = nums[start_zero_at]
                start_zero_at += 1
                
        while start_zero_at < len(nums):
            nums[start_zero_at] = 0
            start_zero_at += 1
        
        return nums
            
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([0,1,0,3,12]), "expected_output": [1,3,12,0,0]},
        {"input": ([0]), "expected_output": [0]},
        {"input": ([1,0]), "expected_output": [1,0]}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.moveZeroes(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    
# TC O(2n) = O(n)
# SC O(1)