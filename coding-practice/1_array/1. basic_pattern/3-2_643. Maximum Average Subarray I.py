# https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = temp = sum(nums[0:k])
        
        for i in range(k, len(nums)):
            temp += nums[i] - nums[i - k]
            max_sum = max(max_sum, temp)
            
        return round(max_sum / k, 5)
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([1,12,-5,-6,50,3], 4), "expected_output": 12.75000},
        {"input": ([5], 1), "expected_output": 5.00000}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.findMaxAverage(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    # TC O(k) + O(k - n) = O(n)
    # SC O(1)