from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums)
        possible_outliers = []
        
        for i in range(n):
            remaining = nums[:i] + nums[i + 1 :]
            
            for j in range(n - 1):
                potential_sum = remaining[j]
                special_numbers = remaining[:j] + remaining[j + 1:]
                
                if sum(special_numbers) == potential_sum:
                    possible_outliers.append(nums[i])
        
        return max(possible_outliers)
        
# TC O(n^3) sum 也是一個 O(n)
# SC O(n) possiible + remaining + special 
        
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        nums_set = set(nums)
        max_outlier = float('-inf')
        
        # For each potential sum x
        for x in nums:
            # Calculate potential outlier y
            y = total - 2 * x
            
            # If y exists in nums and is different from x
            # (or appears at least twice if equal to x)
            if y in nums_set and (y != x or nums.count(y) > 1):
                max_outlier = max(max_outlier, y)
        
        return max_outlier
# TC O(n)
# SC O(n)