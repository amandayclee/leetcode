# Implementation of QuickSort
# pivot is last element
def quickSort(arr: list[int], start: int, end: int) -> list[int]:
    if end - start + 1 <= 1:
        return

    pivot = arr[end]

    # Partition: elements smaller than pivot on left side
    left = start
    for right in range(start, end):
        if arr[right] < pivot:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    # Move pivot in-between left & right sides
    arr[end], arr[left] = arr[left], arr[end]
    
    # Quick sort left side
    quickSort(arr, start, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, end)

    return arr