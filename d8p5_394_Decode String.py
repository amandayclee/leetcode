class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multiplier = 0
        current_string = ""
        
        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == '[':
                stack.append((multiplier, current_string))
                multiplier = 0
                current_string = ""
            elif char == ']':
                last_number, last_string = stack.pop()
                current_string = last_string + current_string * last_number
            else:
                current_string += char
            
            return current_string