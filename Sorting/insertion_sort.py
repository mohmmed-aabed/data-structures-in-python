def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_val = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cur_val:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cur_val


array = [20, 10, 40, 30, 60, 50, 70]
insertion_sort(array)
print(array)
# [10, 20, 30, 40, 50, 60, 70]
