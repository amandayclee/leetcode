from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         result = 0
#         running_sum = 0
#         dic = {}
#         dic[0] = 1
#         for i in range(len(nums)):
#             running_sum += nums[i]
#             if running_sum - k in dic:
#                 result += dic[running_sum - k]
#             dic[running_sum] = dic.get(running_sum, 0) + 1
#         return result


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, running_sum = 0, 0
        prefix_sum_dic = {0: 1}

        for num in nums:
            running_sum += num
            result += prefix_sum_dic.get(running_sum - k, 0)
            prefix_sum_dic[running_sum] = prefix_sum_dic.get(running_sum, 0) + 1

        return result


solution = Solution()
print(solution.subarraySum([1, -1, 1, 1, 1, 1], 3))
