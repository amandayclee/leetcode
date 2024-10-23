from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        
        for start in range(n):
            frequency = defaultdict(int)
            for end in range(start, n):
                frequency[ord(s[end]) - ord('a')] += 1
                if max(frequency.values()) >= k:
                    count += n - end
                    break

        return count