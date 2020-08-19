def large_count_sum(arr):

    if len(arr) == 0:
        return

    current_sum = max_sum = arr[0]

    for i in range(1, len(arr)):
        if current_sum + arr[i] <= arr[i]:
            current_sum = arr[i]
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


print(large_count_sum([-1, -3, 4, 5, -1, 10, -6]))
print(large_count_sum([-1, 3, -4, -5, -1, -10, -6]))
print(large_count_sum([5, -2, -3, 4, 2, -3, 5, 0, -1]))
print(large_count_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_count_sum([3]))
print(large_count_sum([]))
