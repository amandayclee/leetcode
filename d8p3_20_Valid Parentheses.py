class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_to_right = {"(": ")",
                         "[": "]",
                         "{": "}"}
        
        for char in s:
            if char in left_to_right:
                stack.append(char)
            elif not stack or left_to_right[stack.pop()] != char:
                return False
        return not stack
                    