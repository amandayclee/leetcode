from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))
            
        # [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]
        
        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        stack = []
        for pos, spd in sorted(pair, reverse=True):
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
    
# TC O(n log n)
# SC O(n)