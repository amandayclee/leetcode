class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        ans = ""
        for value, symbol in int_to_roman.items():
            while num >= value:
                ans += symbol
                num -= value
        
        return ans
        
Solution().intToRoman(3749)

# TC O(1)
# SC O(1)

def intToRoman(self, num: int) -> str:
    pairs = [
        [1000, 'M'],
        [900, 'CM'],
        [500, 'D'],
        [400, 'CD'],
        [100, 'C'],
        [90, 'XC'],
        [50, 'L'],
        [40, 'XL'],
        [10, 'X'],
        [9, 'IX'],
        [5, 'V'],
        [4, 'IV'],
        [1, 'I']
    ]
    
    ans = ""
    for value, symbol in pairs:
        while num >= value:
            ans += symbol
            num -= value
    
    return ans