# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
from typing import List 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        max_candy = max(candies)
        
        for i in candies:
            if max_candy <= (i + extraCandies):
                results.append(True)
            else:
                results.append(False)
        
        return results
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([2,3,5,1,3], 3), "expected_output": [True,True,True,False,True] },
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.kidsWithCandies(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    # TC O(N)
    # SC O(N)