import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i * - 1 for i in stones]
        heapq.heapify(stones)
        print(stones)
        
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, stone1 - stone2)
            
        return stones[0] * -1
    
Solution().lastStoneWeight([2,7,4,1,8,1])