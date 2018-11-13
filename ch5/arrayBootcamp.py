

def even_odd(A):
    next_even, next_odd = 0, len(A)-1
    while next_even < next_odd:
        if (next_even%2)==0:
            next_even+=1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd-=1


# A = [1, 2, 3, 4, 5, 6]
# B = A
# A.append(42)
# # B[2] =11
# B.insert(0, 11)
# print "A", A
# print A[::-1]
# A = A[::-1]
# print "A", A
# print "B", B
# print 1 in A
# even_odd(A)
# print A

M = [['a', 'b', 'c'], ['d', 'e', 'f']]
x = [x for row in M for x in row]
print x
