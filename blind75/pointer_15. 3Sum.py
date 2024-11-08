from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # 修正：和前一個比較
                continue
            
            target = 0 - nums[i]
            two_sum_result = self.two_sum(target, nums[i + 1:])
            for lst in two_sum_result:
                lst.append(nums[i])
                result.append(lst)
                
        return result
        
    def two_sum(self, target, nums):
        two_sum = []
        left, right = 0, len(nums) - 1
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            
            if curr_sum == target:
                two_sum.append([nums[left], nums[right]])
                left += 1
                right -= 1
                # 找到答案後才跳過重複值
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif curr_sum < target:  # 使用 elif
                left += 1
            else:  # curr_sum > target
                right -= 1
        
        return two_sum