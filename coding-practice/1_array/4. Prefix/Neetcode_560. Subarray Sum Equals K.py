from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        res = 0
        
        for num in nums:
            prefix.append(prefix[-1] + num)

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if prefix[j + 1] - prefix[i] == k:
                    res += 1
        
        return res
    
# TC O(n^2) -> TLE
# SC O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        curr_sum = 0
        res = 0
        
        for num in nums:
            curr_sum += num
            
            res += prefix_count.get(curr_sum - k, 0)
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
            
        return res
    
# TC O(n)
# SC O(n)