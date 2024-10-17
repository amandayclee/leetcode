class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        
        while len(word) < k:
            for i in range(len(word)):
                temp = ord(word[i]) + 1 if ord(word[i]) - ord('z') <= 26 else ord('a')
                word += chr(temp)
            
        return word[k - 1]
    
Solution().kthCharacter(10)