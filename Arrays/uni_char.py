def uni_char(s):

    if len(s) == 0:
        return
    if len(s) == 1:
        return True

    seen = set()

    for ch in s:
        if ch in seen:
            return False
        else:
            seen.add(ch)

    return True


print(uni_char('abc'))
