from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        visited = set()
        
        for row_iter in range(len(board)):
            for col_iter in range(len(board[0])):
                if self.dfs(0, row_iter, col_iter, visited):
                    return True
        
        return False

    def dfs(self, index, row, col, visited):
        if index == len(self.word):
            return True
        
        if row < 0 or row >= len(self.board) or \
            col < 0 or col >= len(self.board[0]) or \
            self.board[row][col] != self.word[index] or \
            (row, col) in visited:
            return False
        
        visited.add((row, col))

        result = (self.dfs(index + 1, row - 1, col, visited) or 
                  self.dfs(index + 1, row + 1, col, visited) or
                  self.dfs(index + 1, row, col - 1, visited) or
                  self.dfs(index + 1, row, col + 1, visited))
        
        visited.remove((row, col))
        
        return result
    

# m is the nubmer of cells in the board
# n is the length of the word
# TC O(m * 4^n)
# SC O(n)

Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")