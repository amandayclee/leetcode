from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        suffix = 1
        
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]
               
        return answer

solution = Solution()
print(solution.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(solution.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]

