class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        choices = list(range(1, maxChoosableInteger + 1))
        if sum(choices) < desiredTotal:
            return False
        
        self.memo = {}
        
        return self.can_win(tuple(choices), desiredTotal)
    
    def can_win(self, choices, remaining_total):
        if choices[-1] >= remaining_total:
            return True
        
        if choices in self.memo:
            return self.memo[choices]
        
        for i in range(len(choices)):
            if not self.can_win(tuple(choices[:i] + choices[i + 1:]), remaining_total - choices[i]):
                self.memo[choices] = True
                return True
            
        self.memo[choices] = False
        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([10, 11]), "expected_output": False},
        {"input": ([10, 0]), "expected_output": True},
        {"input": ([10, 1]), "expected_output": True},
    ]
    for test_case in test_cases:
        assert solution.canIWin(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]
