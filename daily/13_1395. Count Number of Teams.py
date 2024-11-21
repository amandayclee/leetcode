from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        
        for i in range(len(rating)):
            # left
            left_smaller = 0
            left_bigger = 0
            for j in range(0, i):  # 改這裡
                if rating[j] < rating[i]:  # 改這裡
                    left_smaller += 1
                elif rating[j] > rating[i]:
                    left_bigger += 1
            
            # right
            right_smaller = 0
            right_bigger = 0
            for k in range(i + 1, len(rating)):
                if rating[k] < rating[i]:  # 改這裡
                    right_smaller += 1
                elif rating[k] > rating[i]:
                    right_bigger += 1
                    
            res += left_smaller * right_bigger  # 遞增的情況
            res += left_bigger * right_smaller  # 遞減的情況
        
        return res
    
Solution().numTeams([1,2,3,4])

# TC O(N^2)
# SC O(1)