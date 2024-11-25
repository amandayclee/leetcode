from collections import defaultdict


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s) % k != 0:
            return False
        
        s_compare = []
        t_compare = []
        
        substring_length = len(s) // k
        for i in range(0, len(s), substring_length):
            s_compare.append(s[i:i + substring_length])
            t_compare.append(t[i:i + substring_length])
        
        if sorted(s_compare) == sorted(t_compare):
            return True
        return False
    
Solution().isPossibleToRearrange("aabbcc","bccaab", 2)

# TC O(n) + O(k log k * n / k)
# SC O(n)
