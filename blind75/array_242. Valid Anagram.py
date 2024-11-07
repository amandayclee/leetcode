from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        
# TC O(n log n)
# SC O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        
        for i in range(len(s)):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1
            
        return freq_s == freq_t
    
# TC O(n)
# SC O(1) # only use 26 character
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        
        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            freq[s_idx] += 1
            
            t_idx = ord(t[i]) - ord('a')
            freq[t_idx] -= 1
            
        for val in freq:
            if val != 0:
                return False
        return True

# TC O(n)
# SC O(1)