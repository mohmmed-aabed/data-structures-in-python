def balance_check(s):

    if len(s) % 2 != 0:
        return False

    opening = '([{'
    matches = {')': '(', ']': '[', '}': '{'}
    stack = []

    for paren in s:

        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if matches[paren] != last_open:
                return False

    return stack == []


print(balance_check('{{[]}}[]()'))
