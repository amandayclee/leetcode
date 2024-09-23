class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left_rec_area = (ax2 - ax1) * (ay2 - ay1)
        right_rec_area = (bx2 - bx1) * (by2 - by1)
        
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlat_height = min(ay2, by2) - max(ay1, by1)
        overlap_rec_area = max(overlap_width, 0) * max(overlat_height, 0)
        
        return left_rec_area + right_rec_area - overlap_rec_area
    