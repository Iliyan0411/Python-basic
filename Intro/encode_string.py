# aaaaabbbff

def encodeString(s):
    res = ""
    if len(s) == 0: return res

    last_char = s[0]
    counter = 1

    for i in range(1,len(s)):
        if last_char == s[i]: counter += 1
        else:
            if counter <= 2: res += counter * last_char
            else: res += str(counter) + last_char
        
            last_char = s[i]
            counter = 1

    if counter <= 2: res += counter * last_char
    else: res += str(counter) + last_char

    return res


print(encodeString (input('Enter string: ')))