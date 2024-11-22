class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = 1
        numerator = []
        denominator = []
        curr_num = 0
        idx = 0
        
        while idx < len(expression):
            if expression[idx] == '-':
                sign = -1
                idx += 1
            elif expression[idx] == '+':
                sign = 1
                idx += 1
            elif expression[idx] == '/':
                numerator.append(curr_num * sign)
                curr_num = 0
                idx += 1
            elif expression[idx] >= '0' and expression[idx] <= '9':
                curr_num = curr_num * 10 + (ord(expression[idx]) - ord('0'))
                idx += 1
            
            if idx == len(expression) or (idx < len(expression) and (expression[idx] == '+' or expression[idx] == '-')):
                denominator.append(curr_num)
                curr_num = 0

        lcd = self.lcm_list(denominator)
        result = 0
        for i in range(len(numerator)):
            result += numerator[i] * (lcd // denominator[i])

        g = self.gcd(abs(result), lcd)
        return f"{result//g}/{lcd//g}"
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)
        
    def lcm_list(self, arr):
        result = arr[0]
        for i in range(1, len(arr)):
            result = self.lcm(result, arr[i])
        return result

# TC O(n + k log m)
# n = len(expression)
# k = # of numerator
# m = maximum denominator
# gcd / lcm O(log m)
# SC O(k)
Solution().fractionAddition("1/2+1/3")

class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != '-':
            expression = '+' + expression
            
        numerator = 0 
        denominator = 1
        idx = 0
        
        while idx < len(expression):
            # 讀取符號
            sign = 1 if expression[idx] == '+' else -1
            idx += 1
            
            # 讀取分子
            curr_num = 0
            while expression[idx] != '/':
                curr_num = curr_num * 10 + (ord(expression[idx]) - ord('0'))
                idx += 1
            curr_numerator = curr_num * sign
            idx += 1
            
            # 讀取分母
            curr_denominator = 0
            while idx < len(expression) and expression[idx] >= '0' and expression[idx] <= '9':
                curr_denominator = curr_denominator * 10 + (ord(expression[idx]) - ord('0'))
                idx += 1
                
            # 累加分數
            numerator = numerator * curr_denominator + curr_numerator * denominator
            denominator *= curr_denominator
            
            # 化簡
            a, b = abs(numerator), denominator
            while b: 
                a, b = b, a % b
            numerator //= a
            denominator //= a
            
        return f"{numerator}/{denominator}"

# TC O(n)
# SC O(1)

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = {}
        idx = 0
        
        if expression[0] != '-':
            expression = '+' + expression
            
        while idx < len(expression):
            # 讀取符號
            sign = 1 if expression[idx] == '+' else -1
            idx += 1
            
            # 讀取分子
            curr_num = 0
            while expression[idx] != '/':
                curr_num = curr_num * 10 + (ord(expression[idx]) - ord('0'))
                idx += 1
            curr_numerator = curr_num * sign
            idx += 1
            
            # 讀取分母
            curr_denominator = 0
            while idx < len(expression) and expression[idx] >= '0' and expression[idx] <= '9':
                curr_denominator = curr_denominator * 10 + (ord(expression[idx]) - ord('0'))
                idx += 1
                
            fractions[curr_denominator] = fractions.get(curr_denominator, 0) + curr_numerator
        
        numerator = 0
        denominator = 1
        
        for denom, num in fractions.items():
            numerator = numerator * denom + num * denominator  
            denominator *= denom
            
            # 化簡
            a, b = abs(numerator), denominator
            while b:
                a, b = b, a % b
            numerator //= a
            denominator //= a
            
        return f"{numerator}/{denominator}"

# TC O(n)
# SC O(k)