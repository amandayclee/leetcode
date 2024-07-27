from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx, end_idx = 0, len(nums) - 1
        
        while start_idx <= end_idx:
            mid_idx = (start_idx + end_idx) // 2
            if target == nums[mid_idx]:
                return mid_idx
            
            # if mid in the left sorted array
            if nums[start_idx] <= nums[mid_idx]:
                # target is in the right portion
                if (target > nums[mid_idx]) or\
                (target < nums[mid_idx] and target < nums[start_idx]):
                    start_idx = mid_idx + 1
                # target is in the left portion
                else:
                    end_idx = mid_idx - 1
            # if mid in the right sorted array
            else:
                if (target < nums[mid_idx]) or \
                    (target > nums[mid_idx] and target > nums[end_idx]):
                    end_idx = mid_idx - 1
                else:
                    start_idx = mid_idx + 1                   
        return - 1