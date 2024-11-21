class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        
        idx = 0
        ans = 0
        
        while idx <= len(s) - 1:          
            if (idx != len(s) - 1) and (s[idx] == 'I' or s[idx] == 'X' or s[idx] == 'C'):
                if s[idx:idx + 2] in roman_to_int:
                    ans += roman_to_int[s[idx:idx + 2]]
                    idx += 2
                else:
                    ans += roman_to_int[s[idx]]
                    idx += 1
            else:
                ans += roman_to_int[s[idx]]
                idx += 1
        
        return ans
    
# TC O(n)
# SC O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        prev_value = 0
        ans = 0
        
        for char in range(len(s) - 1, -1, -1):
            cur_value = roman_to_int[char]
            if cur_value < prev_value:
                ans -= cur_value
            else:
                ans += cur_value
            prev_value = cur_value
  
# TC O(n)
# SC O(1)
