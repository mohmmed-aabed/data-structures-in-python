def compress(s):

    if len(s) == 0:
        return ''

    cur_ch = s[0]
    ch_num = 1
    output = ''

    for ch in s[1:]:
        if ch == cur_ch:
            ch_num += 1
        else:
            output += '{}{}'.format(cur_ch, ch_num)
            cur_ch = ch
            ch_num = 1

    output += '{}{}'.format(cur_ch, ch_num)

    return output


print(compress('AAABBBCCCaaaaaa'))
print(compress('ABab'))
