def rev_word(s):

    word = ''
    words = []

    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if len(word) > 0:
                words.insert(0, word)
            word = ''

    return ' '.join(words)


print(rev_word('  This is the best  '))
print(rev_word('    How are you?    '))
