from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        
        while low < high:
            mid = low + ((high - low) // 2)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count > mid:
                high = mid
            else:
                low = mid + 1
                
        return low


if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": [1,3,4,2,2], "expected_output": 2}
    ]
    for test_case in test_cases:
        assert solution.findDuplicate(test_case["input"]) == test_case["expected_output"]