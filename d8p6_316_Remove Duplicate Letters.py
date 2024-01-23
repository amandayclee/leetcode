class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # monotonic stack + frequency + visited
        stack = []
        visited = set()
        last_occ = {}
        for idx, char in enumerate(s):
            last_occ[char] = idx
        
        
        for idx, char in enumerate(s):
            if char in visited:
                continue
            else:
                while stack and ord(char) < ord(stack[-1]) and idx < last_occ[stack[-1]]:  # still have chance to add the poped char later if current char idx is smaller than poped char last occur 
                    visited.remove(stack.pop())
                
                stack.append(char)
                visited.add(char)
            
        return "".join(stack)
    
solution = Solution()
print(solution.removeDuplicateLetters("cbacdcbc"))