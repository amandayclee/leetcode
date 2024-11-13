def brute_force(nums):
    max_subarray_sum = float('-inf')

    for start in range(len(nums)):
        temp = 0
        for end in range(start, len(nums)):
            temp += nums[end]
            max_subarray_sum = max(max_subarray_sum, temp)
        return max_subarray_sum
# TC O(n^2)
# SC O(1)

def kadanse(nums):
    max_subarray_sum = float('-inf')
    cur_sum = 0
    
    for num in nums:
        cur_sum = max(cur_sum, 0) + num
        max_subarray_sum = max(max_subarray_sum, cur_sum)
    
    return max_subarray_sum

# TC O(n)
# SC O(1)

def sliding_window(nums):
    max_subarray_sum = float('-inf')
    cur_sum = 0
    max_l, max_r = 0, 0
    L = 0
    
    for R in range(len(nums)):
        if cur_sum < 0:
            cur_sum = 0
            L = R
        
        cur_sum += nums[R]
        if cur_sum > max_subarray_sum:
            max_subarray_sum = cur_sum
            max_l, max_r = L, R
    return [max_l, max_r]

# TC O(n)
# SC O(1)
