from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # check edge (col)
        for row in range(len(board)):
            if board[row][0] == "O":
                self.dfs(row, 0, board)
            if board[row][len(board[0]) - 1] == "O":
                self.dfs(row, len(board[0]) - 1, board)
        
        # check edge (row)
        for col in range(len(board[0])):
            if board[0][col] == "O":
                self.dfs(0, col, board)
            if board[len(board) - 1][col] == "O":
                self.dfs(len(board) - 1, col, board)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"

        
    def dfs(self, row, col, board):
        if (row < 0 or col < 0 or 
            row == len(board) or col == len(board[0]) or
            board[row][col] != "O"):
                return
            
        board[row][col] = "T"
        self.dfs(row + 1, col, board)
        self.dfs(row - 1, col, board)
        self.dfs(row, col + 1, board)
        self.dfs(row, col - 1, board)
        
# TC O(m + n + m*n) -> O(m*n)
# SC O(m*n) dfs traverse all cells