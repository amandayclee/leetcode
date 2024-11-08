from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            length = right - left + 1
            
            if length - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                length = right - left + 1
                
            max_length = max(length, max_length)
        
        return max_length
    
Solution().characterReplacement("AABABBA")

# TC O(n)
# SC O(1) # only 26 upper letter char