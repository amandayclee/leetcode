from typing import List


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = []
#         for start in range(len(temperatures)):
#             for end in range(start, len(temperatures)):
#                 if temperatures[start] < temperatures[end]:
#                     res.append(end - start)
#                     break
#                 elif end == len(temperatures) - 1:
#                     res.append(0)
            
#         return res

# TC O(n^2)
# SC O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, idx]
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append([temp, idx])
            
        return res
        
# TC O(n)
# SC O(n)

Solution().dailyTemperatures([30,38,30,36,35,40,28])