# https://leetcode.com/problems/first-missing-positive/description/
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # we want to put nums[i] to where it's supposed to
                # which is nums[i] - 1 (minus one because of index)
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([1,2,0]), "expected_output": 3},
        {"input": ([3,4,-1,1]), "expected_output": 2},
        {"input": ([7,8,9,11,12]), "expected_output": 1}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.firstMissingPositive(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    # TC O(n)
    # SC O(1)