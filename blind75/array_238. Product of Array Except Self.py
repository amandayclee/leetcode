from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        prefix_product = [1] * (len(nums) + 1)
        suffix_product = [1] * (len(nums) + 1)
        	
        for i in range(len(prefix_product) - 1):
            prefix_product[i + 1] = prefix_product[i] * nums[i]
    
        for i in range(len(suffix_product) - 1, 0, -1):
            suffix_product[i - 1] = suffix_product[i] * nums[i - 1]

        for i in range(len(nums)):
            result.append(prefix_product[i]*suffix_product[i + 1])
            
        return result
    
Solution().productExceptSelf([1, 2, 3, 4])


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # take result as prefix output

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = suffix * result[i]
            suffix *= nums[i]

        return result