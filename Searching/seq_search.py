def seq_search(arr, ele):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1
    return found


print(seq_search([30, 20, 40, 10, 50], 40))
# True
print(seq_search([30, 20, 40, 10, 50], 25))
# False


def ordered_seq_search(arr, ele):
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1
    return found


print(ordered_seq_search([10, 20, 30, 40, 50], 30))
# True
print(ordered_seq_search([10, 20, 30, 40, 50], 45))
# False
