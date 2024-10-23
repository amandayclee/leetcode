# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: list) -> list:
        return self.mergeSort_helper(pairs, 0, len(pairs) - 1)

    def mergeSort_helper(self, arr, start, end):
        if start >= end:
            return arr
        
        mid = (start + end) // 2
        self.mergeSort_helper(arr, start, mid)
        self.mergeSort_helper(arr, mid + 1, end)

        self.merge(arr, start, mid, end)
        return arr

    def merge(self, arr, start, mid, end):
        left_subarray = arr[start:mid + 1]  # This range is inclusive of mid
        right_subarray = arr[mid + 1:end + 1]

        i = 0
        j = 0
        k = start

        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i].key <= right_subarray[j].key:
                arr[k] = left_subarray[i]
                i += 1
            else:
                arr[k] = right_subarray[j]
                j += 1
            k += 1

        while i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
            k += 1

        while j < len(right_subarray):
            arr[k] = right_subarray[j]
            j += 1
            k += 1
