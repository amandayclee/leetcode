from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost_pairs = sorted(zip(nums, cost))

        left_val, right_val = min(nums), max(nums)
        while left_val < right_val:
            median_val = (left_val + right_val) // 2

            if self.compute_cost(nums_cost_pairs, median_val) < self.compute_cost(
                nums_cost_pairs, median_val + 1
            ):
                right_val = median_val
            else:
                left_val = median_val + 1

        return self.compute_cost(nums_cost_pairs, left_val)

    def compute_cost(self, nums_cost_pairs, target_val):
        left_idx, right_idx = 0, len(nums_cost_pairs) - 1
        while left_idx < right_idx:
            mid_idx = left_idx + (right_idx - left_idx) // 2
            temp = nums_cost_pairs[mid_idx][0]
            if temp <= target_val:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx

        cost_left, cost_right = 0, 0

        for i in range(left_idx):
            cost_left += (target_val - nums_cost_pairs[i][0]) * nums_cost_pairs[i][1]
        for i in range(left_idx, len(nums_cost_pairs)):
            cost_right += (nums_cost_pairs[i][0] - target_val) * nums_cost_pairs[i][1]

        return cost_left + cost_right
