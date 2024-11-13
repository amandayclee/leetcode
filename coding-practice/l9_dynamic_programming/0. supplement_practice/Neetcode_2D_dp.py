def brute_force(r, c, rows, cols):
    if r == rows or c == cols: # exceed boundary
        return 0
    
    if r == rows - 1 and c == cols - 1: # find bottom right cell
        return 1
    
    return (brute_force(r + 1, c, rows, cols) +
            brute_force(r, c + 1, rows, cols))

# TC O(2^(n + m)) from 0, 0 -> m-1, n-1 need to go m+n-2 steps
# SC O(m+n) longest path length is m+n-2

def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    
    if cache[r][c] > 0:
        return cache[r][c]
    
    if r == rows - 1 and c == cols - 1:
        return 1
    
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache) + memoization(r, c + 1, rows, cols, cache))
    
    return cache[r][c]

# TC O(m * n)
# SC O(m * n)

def dp(rows, cols):
    prev_row = [0] * cols
    
    for i in range(rows - 1, -1, -1): # from bottow row
        cur_row = [0] * cols
        cur_row[-1] = 1
        for c in range(cols - 2, -1, -1):
            cur_row[c] = cur_row[c + 1] + prev_row[c]
        prev_row = cur_row
    return prev_row[0]

# TC O(m * n) m = rows
# SC O(n) n = cols