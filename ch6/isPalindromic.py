
def isPalindromic(s):
    # s[~i] for i in [0, len(s)-1] is s[-(i+1)]
    return all(s[i]==s[~i] for i in range(len(s)//2))

s = 'abcdefg'
print 's ', s
print 'len(s) ', len(s)
print [i for i in range(len(s)//2)]
