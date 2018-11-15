
import collections

def canFormPalindrome(s):
    return sum(v%2 for v in collections.Counter(s).values()) <= 1

s = 'level'

print s, ' : ',  canFormPalindrome(s)

s = 'rotator'

print s, ' : ', canFormPalindrome(s)

s = 'edifi'

print s, ' : ', canFormPalindrome(s)

