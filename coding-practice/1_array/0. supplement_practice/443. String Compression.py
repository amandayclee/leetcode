from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 1
        
        while left <= right and right < len(chars):
            if chars[left] == chars[right]:
                right += 1
            else:
                if (right - left) != 1:
                    chars[left + 1:right] = [i for i in str(right - left)]
                    left += len(str(right - left)) + 1
                    right = left + 1
                else:
                    left += 1
                    right = left + 1
                
        if (right - left) != 1:
            chars[left+1:right] = [i for i in str(right - left)]
            
        return len(chars)

# TC O(N)
# SC O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = left = 0
        
        for right in range(len(chars) + 1): # handle the last element
            if right == len(chars) or chars[right] != chars[left]:
                chars[write] = chars[left]
                write += 1
                
                if right - left > 1:
                    count = str(right - left)
                    for digit in count:
                        chars[write] = digit
                        write += 1
                
                left = right
        
        return write
    
# TC O(N)
# SC O(1)