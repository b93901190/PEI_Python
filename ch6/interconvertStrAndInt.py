import string

def intToString(x):
    isNeg = False
    if x < 0 :
        x, isNeg = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x%10))
        x //= 10
        if x==0:
            break
    return ('-' if isNeg else '') + ''.join(reversed(s))

def strToInt(s):
    return reduce(lambda running_sum, c : running_sum*10 + string.digits.index(c), s[s[0]=='-':], 0) * (-1 if s[0]=='-' else 1)

x = 1000000000000000000

str = intToString(x)
print str

print strToInt(str)