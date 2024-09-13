# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        temp = 0
        min_length = float('inf')
        
        for right in range(n):
            temp += nums[right]
            while temp >= target:
                min_length = min(min_length, right - left + 1)
                temp -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (7, [2,3,1,2,4,3]), "expected_output": 2},
        {"input": (4, [1,4,4]), "expected_output": 1},
        {"input": (11, [1,1,1,1,1,1,1,1]), "expected_output": 0}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.minSubArrayLen(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
# TC O(n) + 最壞的情況下 while loop 是 O(n) = O(2n) = O(n)
# SC O(1)