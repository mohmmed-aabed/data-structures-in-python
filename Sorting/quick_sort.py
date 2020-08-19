def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, first, last):
    if first < last:
        split_point = partition(arr, first, last)
        _quick_sort(arr, first, split_point - 1)
        _quick_sort(arr, split_point + 1, last)


def partition(arr, first, last):
    pivot_value = arr[first]
    left_mark = first + 1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1

        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp

    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp

    return right_mark


array = [15, 22, 13, 27, 12, 10, 20, 25]
quick_sort(array)
print(array)
# [10, 12, 13, 15, 20, 22, 25, 27]
