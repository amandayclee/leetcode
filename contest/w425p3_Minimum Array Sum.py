from functools import cache
import math
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        # 計算每個數字的所有可能操作結果
        operations = []  # [(原始值, 最終值, op1使用次數, op2使用次數), ...]
        
        for num in nums:
            curr_ops = []
            # 不操作
            curr_ops.append((num, num, 0, 0))
            
            # 只用 op1
            val1 = math.ceil(num / 2)
            if val1 < num:
                curr_ops.append((num, val1, 1, 0))
            
            # 只用 op2
            if num >= k:
                val2 = num - k
                curr_ops.append((num, val2, 0, 1))
                
                # op2 後 op1
                val3 = math.ceil(val2 / 2)
                if val3 < val2:
                    curr_ops.append((num, val3, 1, 1))
            
            # op1 後 op2
            if val1 >= k:
                val4 = val1 - k
                curr_ops.append((num, val4, 1, 1))
            
            # 選擇收益最大的操作（原始值-最終值最大）
            curr_ops.sort(key=lambda x: x[0] - x[1], reverse=True)
            operations.append(curr_ops)
        
        # DP 解決背包問題
        @cache
        def dp(index, rem_op1, rem_op2):
            if index == len(nums):
                return 0
            
            min_sum = float('inf')
            # 嘗試當前數字的每種可能操作
            for _, final_val, need_op1, need_op2 in operations[index]:
                if need_op1 <= rem_op1 and need_op2 <= rem_op2:
                    curr_sum = final_val + dp(index + 1, rem_op1 - need_op1, rem_op2 - need_op2)
                    min_sum = min(min_sum, curr_sum)
            
            return min_sum
        
        return dp(0, op1, op2)