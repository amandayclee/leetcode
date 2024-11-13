from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        
        
        for num in nums1:
            if num not in set(nums2) and num not in set(answer[0]):
                answer[0].append(num)
                
        for num in nums2:
            if num not in set(nums1) and num not in set(answer[1]):
                answer[1].append(num)
                
        return answer
    
Solution().findDifference([1,2,3], [2,4,6])

# TC O(m+n)
# SC O(m+n)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return [list(set1 - set2), list(set2 - set1)]
    
# TC O(m+n)
# SC O(m+n)