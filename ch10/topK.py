import heapq
import itertools

def topK(k, stream):
    minHeap = [(len(s), s) for s in stream[:k]]
    heapq.heapify(minHeap)

    for nextStr in stream[k:]:
        heapq.heappushpop(minHeap, (len(nextStr), nextStr))

    return [p[1] for p in heapq.nsmallest(k, minHeap)]


stream = 'eorigherg', 'wefwefw', 'rtrthrthfergerg', 'tgej', '09u34t'

print topK(3, stream)

