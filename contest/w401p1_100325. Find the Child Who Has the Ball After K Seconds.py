class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # 兩個正整數 n, k
        # queue [0, 1, ..., n-1]
        # 從 0 開始往右丟球，打到邊界往回打
        # 經過 k 秒後誰會拿到球
        
        # k 必大於 0
        # n 必大於 2 [0, 1, 2]
        
        if k < (n - 1):
            return k
        
        if (k % ((n - 1) * 2)) == 0:
            return 0
        
        if (k % ((n - 1))) == 0:
            return (n - 1)
        
        if (k // (n - 1) % 2) != 0:
            return (n - 1) - (k % (n - 1))
        else:
            return (k % (n - 1))
        
        # 每過 (n - 1) * 2 會變成 0
        