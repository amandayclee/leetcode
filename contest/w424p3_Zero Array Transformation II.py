from typing import List


class Solution:
   def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
       n = len(nums)
       
       def can_reduce_to_zero(m):
           """
           檢查使用前m個queries是否能讓數組全部變成0
           使用差分數組來處理區間修改
           """
           # 建立差分數組
           diff = [0] * (n + 1)
           
           # 處理前m個query的差分標記
           for i in range(m):
               left, right, val = queries[i]
               diff[left] += val      # 區間起點加上val
               diff[right + 1] -= val # 區間終點後減去val
               
           # 用前綴和計算每個位置實際可以減少的值
           curr_sum = 0
           for i in range(n):
               curr_sum += diff[i]
               # 如果當前位置減不到0，返回False
               if curr_sum < nums[i]:
                   return False
           return True
           
       # 如果使用全部queries都無法讓數組變成0，直接返回-1    
       if not can_reduce_to_zero(len(queries)):
           return -1
           
       # 二分搜索找最小的可行解
       left, right = 0, len(queries)
       while left <= right:
           mid = left + (right - left) // 2
           
           if can_reduce_to_zero(mid):
               # mid個queries可以，試試更少的
               right = mid - 1
           else:
               # mid個queries不夠，試試更多的
               left = mid + 1
               
       return left
    
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)  # 差分數組
        s = k = 0  # s是前綴和，k是需要的query數量
        
        # 從左到右遍歷nums的每個位置
        for i in range(n):
            # 如果目前累積的和不夠減少nums[i]
            while s + cnt[i] < nums[i]:
                k += 1  # 需要多一個query
                if k - 1 >= len(queries):  # 如果超出queries數量
                    return -1
                    
                # 取得第k個query
                l, r, val = queries[k - 1]
                if r < i:  # 如果這個query不能影響當前位置
                    continue
                    
                # 用差分數組標記這個query的影響
                cnt[max(l, i)] += val  # 從max(l,i)開始加
                cnt[r + 1] -= val
                
            s += cnt[i]  # 更新前綴和
            
        return k