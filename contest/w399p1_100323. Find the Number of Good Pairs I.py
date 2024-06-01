from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2_times_k = [ x * k for x in nums2 ]
        good_count = 0
        
        for i in nums1:
            for j in nums2_times_k:
                if i % j == 0:
                    good_count += 1
        
        return good_count
    
solution = Solution()
print(solution.numberOfPairs([1,3,4], [1,3,4], 1))