from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for num in nums:
            if num - 1 not in nums_set:
                length = 1
                
                while num + length in nums_set:
                    length += 1
            
                max_length = max(length, max_length)
                
        return max_length
    

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([100,4,200,1,3,2]), "expected_output": (4)},
        {"input": ([0,3,7,2,5,8,4,6,0,1]), "expected_output": (9)},
    ]
    for test_case in test_cases:
        assert solution.longestConsecutive(test_case["input"]) == test_case["expected_output"]