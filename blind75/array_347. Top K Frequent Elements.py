from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        unique_nums = list(freq.keys())

        target_idx = k - 1
        start_idx, end_idx = 0, len(unique_nums) - 1

        return self.quick_select(unique_nums, freq, target_idx, start_idx, end_idx)

    def quick_select(self, unique_nums, freq, target_idx, start_idx, end_idx):
        if start_idx == end_idx:
            return unique_nums[:start_idx + 1]

        pivot_idx = self.partition(unique_nums, freq, start_idx, end_idx)

        if pivot_idx < target_idx:
            return self.quick_select(unique_nums, freq, target_idx, pivot_idx + 1, end_idx)
        elif pivot_idx > target_idx:
            return self.quick_select(unique_nums, freq, target_idx, start_idx, pivot_idx - 1)
        else:
            return unique_nums[:pivot_idx + 1]

    def partition(sefl, unique_nums, freq, start_idx, end_idx):
        mid_idx = (start_idx + end_idx) // 2
        pivot_freq = freq[unique_nums[mid_idx]]

        unique_nums[mid_idx], unique_nums[end_idx] = unique_nums[end_idx], unique_nums[mid_idx]

        i = start_idx - 1

        for j in range(start_idx, end_idx):
            if freq[unique_nums[j]] >= pivot_freq:
                i += 1
                unique_nums[i], unique_nums[j] = unique_nums[j], unique_nums[i]
        
        unique_nums[i + 1], unique_nums[end_idx] = unique_nums[end_idx], unique_nums[i + 1]

        return i + 1