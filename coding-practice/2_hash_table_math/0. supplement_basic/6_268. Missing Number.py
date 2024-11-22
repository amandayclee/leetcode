from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pop_lst = [i for i in range(len(nums) + 1)]

        for num in nums:
            if num in pop_lst:
                pop_lst.remove(num)

        return pop_lst[0]
    
# TC O(n^2)
# SC O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        for num in range(len(nums) + 1):
            if num not in num_set:
                return num
            
# TC O(n)
# SC O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # arithmetic aequence
        # sum = n * (a1 + an) / 2
        expected_sum = len(nums) * (1 + len(nums)) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum

# TC O(n)
# SC O(1)