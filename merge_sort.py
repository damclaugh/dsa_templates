
# O(nlog n)
# space is O(n) b/c data is copied into new arrays
# merge sort used in python built-in sort algorithm

def merge_sort(arr):
    # exit when left and right are just one element
    if len(arr) <= 1:
        return arr 

    # otherwise, find midpoint
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # call merge_sort recursively on left and right half
    left = merge_sort(left)
    right = merge_sort(right)

    # merge two halves
    return merge(left, right)

# merges two sorted lists
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # move through the lists with two pointers until end of one
    while left_index < len(left) and right_index < len(right):
        # if left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
           merged.append(right[right_index])
           right_index += 1
        # otherwise append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # append leftovers which are already sorted
    merged += left[left_index:]
    merged += right[right_index:]

    return merged

lst = [8, 3, 1, 7, 0, 10, 2]
print(merge_sort(lst))

a = [5,8,12,56,89]
b = [7,9,45,51]
print(merge(a,b))