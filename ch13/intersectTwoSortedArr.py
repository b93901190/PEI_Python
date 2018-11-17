
def intersectOfTwoArr(A, B):
    i, j, intersect = 0, 0, []
    while i<len(A) and j<len(B):
        if A[i]==B[j]:
            if i==0 or A[i]!=A[i-1]:
                intersect.append(A[i])
            i, j = i+1, j+1
        elif A[i] < B[j]:
            i += 1
        else:
            j+=1
    return intersect


A = [2, 3, 3,5, 7, 15]
B = [3,3,7,15,31]

print intersectOfTwoArr(A, B)

