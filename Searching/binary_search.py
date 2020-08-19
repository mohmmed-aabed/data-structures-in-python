def binary_search(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == ele:
            found = True
        else:
            if ele > arr[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found


print(binary_search([10, 20, 30, 40, 50], 30))
# True
print(binary_search([10, 20, 30, 40, 50], 45))
# False


def rec_bin_search(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == ele:
            return True
        else:
            if ele > arr[mid]:
                return rec_bin_search(arr[mid + 1:], ele)
            else:
                return rec_bin_search(arr[:mid], ele)


print(rec_bin_search([10, 20, 30, 40, 50], 30))
# True
print(rec_bin_search([10, 20, 30, 40, 50], 15))
# False
