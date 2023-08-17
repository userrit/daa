def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    
    # Merge the sorted halves
    merged = merge(left_half, right_half)
    return merged

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    # Compare elements from the left and right halves and merge them
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Append remaining elements if any
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
