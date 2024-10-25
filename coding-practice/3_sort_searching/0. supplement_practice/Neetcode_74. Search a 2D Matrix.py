from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1 # 4
        left, right = 0, len(matrix) - 1 
        
        while left <= right:
            mid = (left + right) // 2 
            
            if matrix[mid][n] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else: # matrix[mid][0] <= target and matrix[mid][n] >= target)
                inside_left, inside_right = 0, n
                while inside_left <= inside_right:
                    inside_mid = (inside_left + inside_right) // 2 # 1
                    if matrix[mid][inside_mid] < target:
                        inside_left = inside_mid + 1 # 1, 1
                    elif matrix[mid][inside_mid] > target:
                        inside_right = inside_mid - 1 # 0, 1
                    else:
                        return True
                return False
        return False
