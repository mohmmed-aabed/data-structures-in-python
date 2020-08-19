from collections import defaultdict


def finder(arr1, arr2):

    my_dict = defaultdict(int)

    for num in arr2:
        my_dict[num] += 1

    for num in arr1:
        if my_dict[num] == 0:
            return num
        else:
            my_dict[num] -= 1


print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 5, 6]))
