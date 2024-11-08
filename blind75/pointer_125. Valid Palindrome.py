class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric
        temp = ""

        for char in s:
            if (ord(char) > ord('9') or ord(char) < ord('0')) and (ord(char.lower()) > ord('z') or ord(char.lower()) < ord('a')):
                continue
            temp += char.lower()

        print(temp)

        left, right = 0, len(temp) - 1

        while left <= right:
            if temp[left] == temp[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left <= right and not self.is_alphanumeric(s[left]):
                left += 1
            while left <= right and not self.is_alphanumeric(s[right]):
                right -= 1
                
            if left < right:
                if s[left].lower() != s[right].lower() :
                    return False
                else:
                    left += 1
                    right -= 1
                
        return True
            
    def is_alphanumeric(self, char):
        char = char.lower()
        return ('0' <= char <= '9') or ('a' <= char <= 'z')
            