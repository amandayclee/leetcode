# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k - 1, 0, len(nums) - 1)

    def quick_select(self, nums, target_index, start_idx, end_idx):
        pivot_index = self.partition(nums, start_idx, end_idx)

        if pivot_index < target_index:
            return self.quick_select(nums, target_index, pivot_index + 1, end_idx)
        elif pivot_index > target_index:
            return self.quick_select(nums, target_index, start_idx, pivot_index - 1)
        else:
            return nums[pivot_index]

    def partition(self, nums, start_idx, end_idx):
        mid_idx = (start_idx + end_idx) // 2
        pivot = nums[mid_idx]

        self.swap(nums, mid_idx, end_idx)

        left_idx, right_idx = start_idx, end_idx - 1
        while left_idx <= right_idx:
            while left_idx <= right_idx and pivot < nums[left_idx]:
                left_idx += 1
            while left_idx <= right_idx and pivot > nums[right_idx]:
                right_idx -= 1
            if left_idx <= right_idx:
                self.swap(nums, left_idx, right_idx)
                left_idx += 1
                right_idx -= 1
        self.swap(nums, left_idx, end_idx)
        return left_idx

    def swap(self, nums, first_idx, second_idx):
        nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]


solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
