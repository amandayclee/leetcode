from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        left, right = 1, max(piles)
        
        res = right
        while left <= right:
            mid = (left + right) // 2
            
            test_k = self.eatBananaPerK(mid)
            if test_k > h:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1
        return res
    
    def eatBananaPerK(self, k):
        hours = 0
        for pile in self.piles:
            hours += (pile + k - 1) // k
            
        return hours
    
Solution().minEatingSpeed([312884470], 312884469)