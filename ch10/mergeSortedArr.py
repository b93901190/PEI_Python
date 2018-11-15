import heapq

def mergeSortedArr(sortedArrs):
    sortedArrIters = [iter(x) for x in sortedArrs]

    minHeap = []

    for i, it in enumerate(sortedArrIters):
        firstElement = next(it, None)
        if firstElement is not None:
            heapq.heappush(minHeap, (firstElement, i))

    result = []
    while minHeap:
        smallestEntry, smallestArrIndex = heapq.heappop(minHeap)
        smallestIter = sortedArrIters[smallestArrIndex]
        result.append(smallestEntry)

        nextElement = next(smallestIter, None)

        if nextElement is not None:
            heapq.heapqpush(minHeap, (nextElement, smallestArrIndex))

    return result

def mergeSortedArrPython(sortedArrs):
    return list(heapq.merge(*sortedArrs))

