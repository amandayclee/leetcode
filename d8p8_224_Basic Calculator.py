class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operator = 1
        calculation = 0

        for char in s:
            if char == ' ':
                continue
            elif char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in ['+', '-']:
                calculation += current_number * operator
                if char == '+':
                    operator = 1
                elif char == '-':
                    operator = -1
                current_number = 0
            elif char == '(':  # start a new cal
                stack.append(calculation)
                stack.append(operator)
                calculation = 0
                operator = 1
            elif char == ')':
                calculation += current_number * operator
                
                calculation *= stack.pop()  # operator
                calculation += stack.pop()  # cal in last ()
                
                current_number = 0
        
        calculation += current_number * operator
        
        return calculation
                
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ("1 + 1"), "expected_output": 2},
        {"input": (" 2-1 + 2 "), "expected_output": 3}
    ]
    for test_case in test_cases:
        assert solution.calculate(test_case["input"]) == test_case["expected_output"]
        

            