from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        unique_nums = list(freq.keys())
        print('test', unique_nums)
        return self.quick_select(unique_nums, freq, k - 1, 0, len(unique_nums) - 1)

    def quick_select(self, unique_nums, freq, target_index, start_idx, end_idx):
        if start_idx == end_idx:
            return unique_nums[:target_index + 1]

        pivot_index = self.partition(unique_nums, freq, start_idx, end_idx)

        if pivot_index < target_index:
            return self.quick_select(unique_nums, freq, target_index, pivot_index + 1, end_idx)
        elif pivot_index > target_index:
            return self.quick_select(unique_nums, freq, target_index, start_idx, pivot_index - 1)
        else:
            return unique_nums[:target_index + 1]
    
    def partition(self, unique_nums, freq, start_idx, end_idx):
        mid_idx = (start_idx + end_idx) // 2
        pivot_freq = freq[unique_nums[mid_idx]]

        self.swap(unique_nums, mid_idx, end_idx)

        left_idx, right_idx = start_idx, end_idx - 1 # new pivot is in the last position
        while left_idx <= right_idx:
            while left_idx <= right_idx and pivot_freq < freq[unique_nums[left_idx]]:
                left_idx += 1
            while left_idx <= right_idx and pivot_freq > freq[unique_nums[right_idx]]:
                right_idx -= 1
            if left_idx <= right_idx:
                self.swap(unique_nums, left_idx, right_idx)
                left_idx += 1
                right_idx -= 1
        self.swap(unique_nums, left_idx, end_idx)
        return left_idx

    def swap(self, unique_nums, first_idx, second_idx):
        unique_nums[first_idx], unique_nums[second_idx] = unique_nums[second_idx], unique_nums[first_idx]
        

solution = Solution()
print(solution.topKFrequent([2, 2, 1, 1, 1, 3], 2))