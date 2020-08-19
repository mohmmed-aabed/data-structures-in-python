from collections import defaultdict


def anagram(s1, s2):

    count = defaultdict(int)
    s1 = s1.replace(' ', '').upper()
    s2 = s2.replace(' ', '').upper()

    if len(s1) != len(s2):
        return False

    for ch in s1:
        count[ch] += 1

    for ch in s2:
        count[ch] -= 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram('Public relations', 'crap built on lies'))
