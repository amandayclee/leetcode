from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in memo:
                return memo[(i, m, n)]
            
            m_cnt, n_cnt = strs[i].count("0"), strs[i].count("1")
            memo[(i, m, n)] = dfs(i + 1, m, n)
            if m_cnt <= m and n_cnt <=  n:
                memo[(i, m, n)] = max(
                    1 + dfs(i + 1, m - m_cnt, n - n_cnt),
                    memo[(i, m, n)] # current
                    )   
            return memo[(i, m, n)]
        
        return dfs(0, m, n)