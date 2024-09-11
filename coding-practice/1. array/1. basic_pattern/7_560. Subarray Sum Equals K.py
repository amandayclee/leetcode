# https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, current_sum = 0, 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for num in nums:
            current_sum += num
            count += prefix_counts[current_sum - k]
            prefix_counts[current_sum] += 1
        return count
        
        
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([1,1,1], 2), "expected_output": 2},
        {"input": ([1,2,3], 3), "expected_output": 2},
        {"input": ([3,4,7,2,-3], 7), "expected_output": 2},
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.subarraySum(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    # TC O(n)
    # SC O(1)