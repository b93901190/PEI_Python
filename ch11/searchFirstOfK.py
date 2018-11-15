
def searchFirstOfK(A, k):
    left, right, result = 0, len(A)-1, -1

    while left<=right:
        mid = left + (right-left)//2
        if A[mid] == k:
            result = mid
            right = mid - 1
        elif A[mid]>k:
            right = mid - 1 # Nothing to the right of mid can be solution
        else:
            left = mid + 1

    return result

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

k = 108
print 'find first index of %d is ' % k, searchFirstOfK(A, k)
k = 285
print 'find first index of %d is ' % k, searchFirstOfK(A, k)

k = 0
print 'find first index of %d is ' % k, searchFirstOfK(A, k)