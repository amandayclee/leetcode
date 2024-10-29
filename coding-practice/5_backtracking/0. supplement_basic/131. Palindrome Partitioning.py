from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.s = s
        self.dfs_helper(0, [])
        
        return self.res
    
    def is_palindrome(self, left, right):
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def dfs_helper(self, start, temp):
        if start >= len(self.s):
            self.res.append(temp[:])
            return
        
        for curr_idx in range(start, len(self.s)):
            if self.is_palindrome(start, curr_idx):
                temp.append(self.s[start:curr_idx + 1])
                self.dfs_helper(curr_idx + 1, temp)
                temp.pop()
    

Solution().partition("aab")
