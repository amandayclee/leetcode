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
    
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([1, -1, 1, 1, 1, 1], 3), "expected_output": 2},
        {"input": ([1, -1, 1, 1, 1, 1], 3), "expected_output": 2}
    ]
    for test_case in test_cases:
        assert solution.subarraySum(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]
        

