from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = [['.' for _ in range(n)] for _ in range(n) ]
        res = []
        self.dfs(boards, n, 0, res)
        return res
        
    def dfs(self, boards, n, row, res):
        if n == row:
            temp = []
            for row in boards:
                temp.append(''.join(row))
            res.append(temp)
            return
        
        for col in range(n):
            if not self.is_valid(boards, col, row):
                continue
            
            boards[row][col] = "Q"
            self.dfs(boards, n, row + 1, res)
            boards[row][col] = "."
            
    def is_valid(self, boards, col, row):
        # up
        for up_row in range(row -1, -1, -1):
            if boards[up_row][col] == "Q":
                return False
            
        # top left
        up_left_row = row - 1
        up_left_col = col - 1
        
        while up_left_row > -1 and up_left_col > -1:
            if boards[up_left_row][up_left_col] == "Q":
                return False
            up_left_row -= 1
            up_left_col -= 1
        
        # top right
        up_right_row = row - 1
        up_right_col = col + 1
        n = len(boards)
        
        while up_right_row > -1 and up_right_col < n:
            if boards[up_right_row][up_right_col] == "Q":
                return False
            up_right_row -= 1
            up_right_col += 1
        
        return True
    

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (4), "expected_output": [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]},
        {"input": (1), "expected_output": [["Q"]]}
    ]
    for test_case in test_cases:
        assert solution.solveNQueens(test_case["input"]) == test_case["expected_output"]
        