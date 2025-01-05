from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def array_gcd(arr):
            # Start with first number
            result = arr[0]
            # Calculate GCD with each subsequent number
            for i in range(1, len(arr)):
                result = gcd(result, arr[i])
            return result
        
        def array_lcm(arr):
            # Start with first number
            result = arr[0]
            # Calculate LCM with each subsequent number
            for i in range(1, len(arr)):
                # LCM(a,b) = (a*b)/GCD(a,b)
                result = (result * arr[i]) // gcd(result, arr[i])
            return result
        
        def array_product(arr):
            # Start with 1
            result = 1
            # Multiply with each number
            for num in arr:
                result *= num
            return result
        
        n = len(nums)
        max_length = 0
        
        # Try all possible subarrays
        for left in range(n):
            for right in range(left, n):
                # Get current subarray
                curr = nums[left:right + 1]
                
                # Calculate product, GCD, LCM
                product = array_product(curr)
                curr_gcd = array_gcd(curr)
                curr_lcm = array_lcm(curr)
                
                # Check if product equivalent
                if product == curr_gcd * curr_lcm:
                    max_length = max(max_length, right - left + 1)
        
        return max_length