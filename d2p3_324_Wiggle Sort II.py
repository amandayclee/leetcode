from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length % 2 == 0:
            mid_idx = length // 2 - 1
        else:
            mid_idx = length // 2

        median = self.quick_select(nums, mid_idx)
        print("before final", nums)
        # Three-way partition
        forward_idx, check_idx, backward_idx = 0, 0, length - 1
        while check_idx <= backward_idx:
            if nums[check_idx] > median:
                nums[check_idx], nums[backward_idx] = (
                    nums[backward_idx],
                    nums[check_idx],
                )
                backward_idx -= 1
            elif nums[check_idx] < median:
                nums[forward_idx], nums[check_idx] = nums[check_idx], nums[forward_idx]
                forward_idx += 1
                check_idx += 1
            else:
                check_idx += 1

        print("final", nums)

        temp1 = nums[: mid_idx + 1]
        temp2 = nums[mid_idx + 1 :]

        print("temp1", temp1)
        print("temp2", temp2)

        for i in range(len(temp1)):
            nums[2 * i] = temp1[-1 - i]
        for i in range(len(temp2)):
            nums[2 * i + 1] = temp2[-1 - i]

    def quick_select(self, nums, target_idx):
        left_idx, right_idx = 0, len(nums) - 1
        while True:
            pivot_idx = self.partition(nums, left_idx, right_idx, target_idx)
            if pivot_idx == target_idx:
                return nums[pivot_idx]
            elif pivot_idx < target_idx:
                left_idx = pivot_idx + 1
            else:
                right_idx = pivot_idx - 1

    def partition(self, nums, left_idx, right_idx, pivot_idx):
        pivot = nums[pivot_idx]
        self.swap(nums, pivot_idx, right_idx)
        store_index = left_idx

        for i in range(left_idx, right_idx):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        self.swap(nums, store_index, right_idx)
        return store_index

    def swap(self, nums, first_idx, second_idx):
        nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]


solution = Solution()
nums = [1, 1, 2, 1, 2, 2, 1]
solution.wiggleSort(nums)
print(nums)
