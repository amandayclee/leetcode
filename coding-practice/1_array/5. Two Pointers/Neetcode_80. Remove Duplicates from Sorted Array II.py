from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left, right = 0, 0

#         while right < len(nums):
#             count = 1

#             while right + 1 < len(nums) and nums[right] == nums[right + 1]:
#                 count += 1
#                 right += 1
            
#             # stop at nums[right] find a different num than nums[left]

#             for i in range(min(2, count)):
#                 nums[left] = nums[right]
#                 left += 1

#             right += 1
        
#         return left
                
# # TC O(N)
# # SC O(1)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left = 2
        
#         for right in range(2, len(nums)):
#             if nums[right] != nums[left - 2]:
#                 nums[left] = nums[right]
#                 left += 1
        
#         return left


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        
        for right in range(len(nums)):
            if left < 2 or nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        
        return left


Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])