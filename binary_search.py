

# applies to sorted list
# time complexity is O(log n)

def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if array[mid_index] == target:
            return mid_index

        if target < array[mid_index]: # search left
            end_index = mid_index - 1

        else: # search right
            start_index = mid_index + 1
    
    return -1

# TEST CASES
nums = [-1, 0, 3, 5, 9, 12]
print(binary_search(nums, 9)) # 4

nums = [-10, -9, -1, 0, 3, 5, 9, 27]
print(binary_search(nums, -10)) # 0


# binary search to find insert index for new num in sorted array
def insert_idx(array, num):
    l = 0
    r = len(array)-1

    while l <= r:
        mid = (l + r) // 2
        if array[mid] >= num:
            r = mid - 1
        else:
            l = mid + 1

    return l

nums = [2,6,6,10]
num = 5
print(insert_idx(nums, num)) # 1



