from typing import List

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         running_sum = [0] * len(nums)
#         for i in range(len(nums)):
#             print(sum(nums[:i + 1]))
#             running_sum[i] = sum(nums[:i + 1])
#         print(running_sum)


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums


solution = Solution()
solution.runningSum([1, 1, 1, 1, 1])
