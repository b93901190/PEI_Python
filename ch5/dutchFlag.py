
RED, WHITE, BLUE = range(3)

def dutchFlag(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)-1
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            equal, smaller = equal+1, smaller+1
        elif A[equal]==pivot:
            equal += 1
        else:
            A[equal], A[larger] = A[larger], A[equal]
            larger -= 1

A = [0, 1, 0, 2, 1, 0]
dutchFlag(1, A)
print A