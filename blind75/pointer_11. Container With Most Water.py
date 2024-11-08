from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)     
        
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:            
            bottom_line = right - left
            height_line = min(height[left], height[right])
            
            max_area = max(max_area, bottom_line * height_line)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
    
Solution().maxArea([1,1])

# TC O(n)
# SC O(1)