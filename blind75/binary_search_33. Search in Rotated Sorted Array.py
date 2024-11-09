from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] <= nums[right]:  # 右半部分有序
                if nums[mid] < target <= nums[right]:  # target 在右半部分
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # 左半部分有序
                if nums[left] <= target < nums[mid]:  # target 在左半部分
                    right = mid - 1
                else:
                    left = mid + 1
                
        return -1

Solution().search([1,3], 3)