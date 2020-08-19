def selection_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        index_of_max = 0
        for k in range(1, n + 1):
            if arr[k] > arr[index_of_max]:
                index_of_max = k
        tem = arr[n]
        arr[n] = arr[index_of_max]
        arr[index_of_max] = tem
    return arr


print(selection_sort([20, 10, 1, 5, 7, 3, 9, 2, 15]))
# [1, 2, 3, 5, 7, 9, 10, 15, 20]
