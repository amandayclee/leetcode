# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
            
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([2,7,11,15], 9), "expected_output": [1,2]},
        {"input": ([2,3,4], 6), "expected_output": [1,3]},
        {"input": ([-1,0], -1), "expected_output": [1,2]}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.twoSum(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    # TC O(N)
    # SC O(1)