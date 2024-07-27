from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        n = len(nums)

        while left > -1 and right < n:
            if nums[left] <= nums[right]:
                left += 1
                right += 1
            elif nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                if left > 0:
                    left -= 1
                    right -= 1
                # print("Current statuse:", nums)

        return nums
solution = Solution()
print(solution.sortColors([2,0,1]))