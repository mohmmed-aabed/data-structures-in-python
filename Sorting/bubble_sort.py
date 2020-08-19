def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k + 1]:
                tem = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = tem


array = [20, 10, 1, 5, 7, 3, 9, 2, 15]
bubble_sort(array)
print(array)
# [1, 2, 3, 5, 7, 9]
