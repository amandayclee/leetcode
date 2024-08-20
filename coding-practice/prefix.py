from typing import List

def prefix_sum(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    return prefix_sum
    
# TC O(n)
# SC O(n) 一個長度為 n+1 的數組