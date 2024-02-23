from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.result = set()
        self.board = board
        self.word = word
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(row, col, 0):
                    return True
        return False
        
    def dfs(self, row, col, index):
        if index == len(self.word):
            return True
        
        if (row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.word[index] != self.board[row][col] or (row, col) in self.result):
            return False
        
        self.result.add((row, col))
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in delta:
            if self.dfs(row + dx, col + dy, index + 1):
                return True
            
        self.result.remove((row, col))
        return False
        