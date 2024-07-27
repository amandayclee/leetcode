from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda i : i[1])
        arrows = 1
        arrow_end = points[0][1]
        
        for start, end in points[1:]:
            if start > arrow_end:
                arrows += 1
                arrow_end = end
        
        return arrows
    
solution = Solution()
solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])