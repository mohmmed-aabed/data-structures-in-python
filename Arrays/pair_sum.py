def pair_sum(arr, k):

    if len(arr) < 2:
        return

    seen = []
    output = []

    for num in arr:
        target = k - num
        if target in seen:
            output.append((num, target))
            seen.remove(target)
        else:
            seen.append(num)

    return len(output)


print(pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))
