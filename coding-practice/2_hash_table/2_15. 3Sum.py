from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([-1,0,1,2,-1,-4]), "expected_output": [[-1,-1,2],[-1,0,1]]},
        {"input": ([0,1,1]), "expected_output": []},
        {"input": ([0,0,0]), "expected_output": [[0,0,0]]}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.threeSum(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")