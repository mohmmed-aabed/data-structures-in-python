def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    print('Merging:', arr)


merge_sort([38, 27, 43, 3, 9, 82, 10, 15])
# Merging: [38]
# Merging: [27]
# Merging: [27, 38]
# Merging: [43]
# Merging: [3]
# Merging: [3, 43]
# Merging: [3, 27, 38, 43]
# Merging: [9]
# Merging: [82]
# Merging: [9, 82]
# Merging: [10]
# Merging: [15]
# Merging: [10, 15]
# Merging: [9, 10, 15, 82]
# Merging: [3, 9, 10, 15, 27, 38, 43, 82]
