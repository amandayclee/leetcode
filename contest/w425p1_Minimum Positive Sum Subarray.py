from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefix = [0]
        subarray = []
        
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        for length_between in range(l, r + 1):
            self.calculate_sum(prefix, length_between, subarray)
            
        return min(subarray) if subarray else -1
        
    def calculate_sum(self, prefix, length, subarray):
        for i in range(length, len(prefix)):
            sum = prefix[i] - prefix[i - length]
            if sum > 0:
                subarray.append(sum)
                
Solution().minimumSumSubarray([-2,2,-3,1], 2, 3)

# TC O(n)
# SC O(n)