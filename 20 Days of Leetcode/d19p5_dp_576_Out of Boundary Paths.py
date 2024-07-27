class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ROWS, COLS = m, n
        MOD = 10**9 + 7
        grid = [[0] * COLS for _ in range(ROWS)]
        
        for m in range(1, maxMove + 1):
            tmp = [[0] * COLS for _ in range(ROWS)]
            for r in range(ROWS):
                for c in range(COLS):
                    if r + 1 == ROWS:
                        tmp[r][c] = (tmp[r][c] + 1) % MOD
                    else:
                        tmp[r][c] = (tmp[r][c] + grid[r + 1][c]) % MOD
                    if r - 1 < 0:
                        tmp[r][c] = (tmp[r][c] + 1) % MOD
                    else:
                        tmp[r][c] = (tmp[r][c] + grid[r - 1][c]) % MOD
                    if c + 1 == COLS:
                        tmp[r][c] = (tmp[r][c] + 1) % MOD
                    else:
                        tmp[r][c] = (tmp[r][c] + grid[r][c + 1]) % MOD
                    if c - 1 < 0:
                        tmp[r][c] = (tmp[r][c] + 1) % MOD
                    else:
                        tmp[r][c] = (tmp[r][c] + grid[r][c - 1]) % MOD
                        
            grid = tmp
        
        return grid[startRow][startColumn]