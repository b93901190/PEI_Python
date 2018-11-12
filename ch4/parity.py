#
# complexity O(n)

def parity(x):
    result = 0
    while x:
        result ^= x&1
        x >>= 1
    return result


# complexity O(k)
# x = 00101100, x-1 = 00101011
# x & (x-1) = 00101000
def parity_Ologk(x):
    result  = 0
    while x:
        result ^= 1
        x = x & (x-1)
    return result

def parity_OlogN(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

num = 11
print parity(num)
print parity_Ologk(num)
print parity_OlogN(num)