class Solution:
    def reverseWords(self, s: str) -> str:
        words_lst = s.split()
        left, right = 0, len(words_lst) - 1
        
        while left < right:
            words_lst[left], words_lst[right] = words_lst[right], words_lst[left]
            left += 1
            right -= 1
            
        return ' '.join(words_lst)
    
    # TC O(N)
    # SC O(N)