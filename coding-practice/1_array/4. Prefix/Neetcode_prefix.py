class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
            
    # TC O(n)
    # SC O(n)        
            
    def range_sum(self, left, right):
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left
    
    # TC O(1)
    # SC O(1)