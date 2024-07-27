class Solution:
    def canWin(self, currentState: str) -> bool:
        def canWinHelper(s):
            for i in range(len(s) - 1):
                if s[i:i+2] == "++":
                    new_state = s[:i] + "--" + s[i+2:]
                    
                    # if next move player cannot win
                    # to the upper level player is winning                    
                    if not canWinHelper(new_state): 
                        return True
            return False

        return canWinHelper(currentState)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": '++++', "expected_output": True},
        {"input": '+++++', "expected_output": False},
    ]
    for test_case in test_cases:
        assert solution.canWin(test_case["input"]) == test_case["expected_output"]
