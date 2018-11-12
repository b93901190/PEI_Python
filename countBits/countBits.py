def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x>>=1
    return num_bits

x = 11
print count_bits(x)
