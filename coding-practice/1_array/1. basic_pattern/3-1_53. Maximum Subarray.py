# https://leetcode.com/problems/maximum-subarray/description/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = temp = nums[0]
        
        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i])
            max_sum = max(temp, max_sum)

        return max_sum
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([-2,1,-3,4,-1,2,1,-5,4]), "expected_output": 6},
        {"input": ([1]), "expected_output": 1},
        {"input": ([5,4,-1,7,8]), "expected_output": 23},
        {"input": ([-2,1]), "expected_output": 1},
        {"input": ([-1,-2]), "expected_output": -1}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.maxSubArray(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
# TC O(n)
# SC O(1)