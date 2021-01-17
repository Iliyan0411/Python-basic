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
#------------------------------------------------------

# 3ab4cll
def decodeString(s):
    res = ""
    temp = ""
    for i in range(0, len(s)):
        if s[i] >= '0' and s[i] <= '9': temp += s[i]
        else:
            if len(temp) == 0: res += s[i]
            else:
                res += int(temp) * s[i]
                temp = ""

    return res
#------------------------------------------------------

def fib_iter (n, prev, curr):
    if n == 0: return prev
    if n == 1: return curr

    return fib_iter(n-1, curr, prev+curr)

def fibbonachi (n):
    return fib_iter(n, 0, 1)
#------------------------------------------------------
def printArr(arr):
    for i in range(0, len(arr)): print(arr[i], end=' ')
#------------------------------------------------------
def findMax(arr):
    max = arr[0]

    for el in arr:
        if el > max: max = el
    
    return max

def mySwap(a, b):
    return b, a



def main():
    # print(encodeString (input('Enter string: ')))
    # print(decodeString (input('Enter string: ')))
    # print(fibbonachi (50))
    # print(printArray ())

    # arr = [1,2,3,5,8,9,6,2,4,10,4]
    # print(findMax (arr))

    a = 5
    b = 10

    a, b = mySwap(a, b)

    print (a, b)


main()