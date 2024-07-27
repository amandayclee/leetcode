from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.dfs()
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    return i, j
        return -1, -1  # no empty cell found
    
    def is_valid(self, num, row, col):
        # row
        for i in range(9):
            if self.board[row][i] == num:
                return False
        
        # col
        for i in range(9):
            if self.board[i][col] == num:
                return False
        
        # 3 * 3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
                
        return True            
    
    def dfs(self):
        row, col = self.find_empty()
        if row == -1 and col == -1:
            return True
        
        for num in '123456789':
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                if self.dfs():  # valid and go find the next one
                    return True  # next one doesn't work
                self.board[row][col] = "."
        return False
    

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], "expected_output": [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]}
    ]
    for test_case in test_cases:
        assert solution.solveSudoku(test_case["input"]) == test_case["expected_output"]