from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # abs(i - j) <= k actually means k separators? k + 1 spots
        # for example [1, 2, 3, 1], index nums[0] == nums[3]
        # i and j should be different
        window = set()

        for i in range(len(nums)):
            left = i
            right = i + 1

            window.add(nums[left])

            while right - left <= k and right < len(nums):
                if nums[right] in window:
                    return True
                
                right += 1
            
            window.remove(nums[left])
            
        return False


Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2)