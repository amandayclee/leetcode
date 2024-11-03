import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_dict = []
        
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            
            distance = sqrt(pow(x, 2) + pow(y, 2))
            heap_dict.append((distance, i))
            
        heapq.heapify(heap_dict)
        
        res = []
        for j in range(k):
            res.append(points[heapq.heappop(heap_dict)[1]])
            
        return res

Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)

# O(n) + O(k log n)
# O(n)