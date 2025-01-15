from typing import List

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        
        for number in nums:
            if number != 0:
                total_product *= number
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)
        
        for index, current_number in enumerate(nums):
            if zero_count:
                result[index] = 0 if current_number != 0 else total_product
            else:
                result[index] = total_product // current_number
                
        return result
    

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        prefix_product = [1] * (len(nums) + 1)
        suffix_product = [1] * (len(nums) + 1) # [1, 1, 1, 1, 1]
        
        for i in range(len(prefix_product) - 1): # 0, 1, 2, 3
            prefix_product[i + 1] = prefix_product[i] * nums[i]
            # [1, 2, 3, 4] 
            # [1, 1, 2, 6, 24]
        
        for i in range(len(suffix_product) - 1, 0, -1): # 4, 3, 2, 1
            suffix_product[i - 1] = suffix_product[i] * nums[i - 1]
        
        answers = [1] * len(nums) # [1, 1, 1, 1]
        
        for i in range(len(answers)):
            answers[i] = prefix_product[i] * suffix_product[i + 1]

        return answers

            
    
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

if __name__ == "__main__":
    solution = Solution2()
    
    test_cases = [
        {"input": ([1,2,3,4]), "expected_output": [24,12,8,6]},
        {"input": ([-1,1,0,-3,3]), "expected_output": [0,0,9,0,0]},
    ]
    for test_case in test_cases:
        assert solution.productExceptSelf(test_case["input"]) == test_case["expected_output"]
        

