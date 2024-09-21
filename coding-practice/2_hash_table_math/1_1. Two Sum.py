from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
            
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([2,7,11,15], 9), "expected_output": [0,1]},
        {"input": ([3,2,4], 6), "expected_output": [1,2]},
        {"input": ([3,3], 6), "expected_output": [0,1]}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.twoSum(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")