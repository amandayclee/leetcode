# https://leetcode.com/problems/range-sum-query-immutable/
# Prefix Sum
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
    
    # to right + 1 because we want to find 0 ~ right (to include the end index)
    # to left because we want to find 0 ~ left - 1 (to include the start index)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)