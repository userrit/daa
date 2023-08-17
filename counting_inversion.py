def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_count = count_inversions(arr[:mid])
    right_half, right_count = count_inversions(arr[mid:])
    merged, split_count = merge_and_count(left_half, right_half)
    
    total_count = left_count + right_count + split_count
    return merged, total_count

def merge_and_count(left, right):
    merged = []
    count = 0
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, count

# Example usage
arr = [2, 4, 1, 3, 5]
sorted_arr, inversions = count_inversions(arr)
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)
