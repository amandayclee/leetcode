def sort_even_odd(nums):
    left, right = 0, 0
    n = len(nums)
    
    while right < n:
        # find the next odd number
        if nums[left] % 2 == 1:
            right = left
            # find the next even
            while right < n and nums[right] % 2 == 1:
                right += 1
            if right < n:
                even_num = nums[right]
                # shift the odd till even - 1 index to the right
                # one at a time
                for i in range(right, left, -1):
                    print(i)
                    nums[i] = nums[i-1]
                # move the event number to the left pointer pos
                nums[left] = even_num
        left += 1

    return nums

arr = [3, 8, 5, 12, 9, 4]
print(sort_even_odd(arr))