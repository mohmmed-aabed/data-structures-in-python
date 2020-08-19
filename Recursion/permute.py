def permute(s):

    output = []

    if len(s) == 1:
        output = [s]

    for i, ch in enumerate(s):
        for perm in permute(s[:i] + s[i + 1:]):
            output += [ch + perm]

    return output


print(permute('abc'))
