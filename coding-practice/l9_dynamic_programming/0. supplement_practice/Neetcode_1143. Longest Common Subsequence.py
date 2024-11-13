class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dfs(len(text1) - 1, len(text2) - 1, text1, text2)
    
    def dfs(self, row, col, text1, text2):
        if row < 0 or col < 0:
            return 0
        
        if text1[row] == text2[col]:
            return self.dfs(row - 1, col - 1, text1, text2) + 1
        
        return max(self.dfs(row - 1, col, text1, text2), self.dfs(row, col - 1, text1, text2))

# TC O(2^(m+n))
# SC O(m+n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = {}
        return self.dfs(len(text1) - 1, len(text2) - 1, text1, text2)
    
    def dfs(self, row, col, text1, text2):
        if row < 0 or col < 0:
            return 0
            
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        
        if text1[row] == text2[col]:
            self.memo[(row, col)] = self.dfs(row - 1, col - 1, text1, text2) + 1
        else:
            self.memo[(row, col)] = max(self.dfs(row - 1, col, text1, text2), self.dfs(row, col - 1, text1, text2))
        
        return self.memo[(row, col)]

# memo字典會逐步填入計算過的結果
# key: (row,col), value: LCS長度
# memo = {
#   (2,2): 2,
#   (1,1): 1,
#   ...
# }
# TC: O(m*n) - 每個子問題只計算一次
# SC: O(m*n) - memo字典的大小

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for row in range(1, len(text1) + 1):
            for col in range(1, len(text2) + 1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                    
        return dp[-1][-1]
    
#   ''  a  b  c  d  e   (text1)
# '' 0  0  0  0  0  0
# a  0  1  1  1  1  1
# c  0  1  1  2  2  2
# e  0  1  1  2  2  3   <- 最終答案
# (text2)

# TC O(m * n)
# SC O(m * n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 只保存一行
        dp = [0] * (len(text2) + 1)
        
        for i in range(1, len(text1) + 1):
            # prev_diagonal 保存左上角的值
            prev_diagonal = 0
            
            for j in range(1, len(text2) + 1):
                # 在更新 dp[j] 之前保存它
                temp = dp[j]
                
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev_diagonal + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                    
                # 為下一個位置更新 prev_diagonal
                prev_diagonal = temp
                
        return dp[-1]
    
# 只保存一行，並用prev_diagonal記住左上角的值
# 以text1="abcde", text2="ace"為例，dp陣列的變化：
# 初始：[0,0,0,0]
# 處理'a': [0,1,1,1]
# 處理'c': [0,1,2,2]
# 處理'e': [0,1,2,3]
# TC: O(m*n) - 仍需遍歷所有位置
# SC: O(n) - 只需一行的空間，n是text2的長度