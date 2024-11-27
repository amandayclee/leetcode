from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        while tokens:
            curr = tokens.pop(0)
            
            if curr not in {"+", "-", "*", "/"}:
                stack.append(int(curr))
            else:
                a, b = stack.pop(), stack.pop()
                if curr == "+":
                    stack.append(b + a)
                elif curr == "-":
                    stack.append(b - a)
                elif curr == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
                    
        return stack[0]

Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

# TC O(n)
# SC O(n)