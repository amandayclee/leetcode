class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = [-1] * (n + 1)
        self.memo[0] = 1
        
        return self.dfs(n)
    
    def dfs(self, node_counts):
        if self.memo[node_counts] != -1:
            return self.memo[node_counts]
        
        total_trees = 0
        
        for left_nodes in range(node_counts):
            right_nodes = node_counts - 1 - left_nodes # -1 is root node
            
            total_trees += self.dfs(left_nodes) * self.dfs(right_nodes)
        
        self.memo[node_counts] = total_trees
        
        return self.memo[node_counts]
    
    
# TC O(n^2) n+1 個狀態，每個狀態需要 O(n) 的計算
# SC O(n)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1) 
        dp[0] = 1
        
        for cur_nodes in range(1, n + 1):
            for left_nodes in range(cur_nodes):
                right_nodes = cur_nodes - 1 - left_nodes
                dp[cur_nodes] += dp[left_nodes] * dp[right_nodes]
                
        return dp[n]
    
    
# TC O(n^2) n+1 個狀態，每個狀態需要 O(n) 的計算
# SC O(n)
