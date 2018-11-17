import itertools

def findMaxSubArr(A):
    minSum = maxSum = 0
    for runningSum in itertools.accumulate(A):
        minSum = min(minSum, runningSum)
        maxSum = max(maxSum, runningSum - minSum)
    return maxSum

A = [904, 40, 523, 12, -335, -385, -124, -481, -31]

print(findMaxSubArr(A))