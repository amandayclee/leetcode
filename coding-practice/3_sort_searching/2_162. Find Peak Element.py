from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left    
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": [1,2,3,1], "expected_output": 2},
        {"input": [1,2,1,3,5,6,4], "expected_output": 5}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        result = solution.findPeakElement(input_data)
        assert abs(result - expected_output) < 1e-5, f"Test case failed: {test_case}, got {result} instead of {expected_output}"
    
    print("All test cases passed!")
        
                
                