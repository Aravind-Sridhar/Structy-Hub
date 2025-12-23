def uncompress(s):
    nums = '0123456789'
    i, j = 0,1
    result = ''
    
    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            result += str(s[j] * int(s[i:j]))
            i = j+1
            j = i+1
    return result