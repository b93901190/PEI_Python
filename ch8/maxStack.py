import collections
class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._elementWithCacheMax = []

    def empty(self):
        return len(self._elementWithCacheMax) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._elementWithCacheMax[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._elementWithCacheMax.pop().element

    def push(self, x):
        self._elementWithCacheMax.append(self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))


class Stack1:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._element = []
        self._cachedMaxWithCount = []

    def empty(self):
        return len(self._element)==0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cachedMaxWithCount[-1].max

    def push(self, x):
        self._element.append(x)

        if len(self._cachedMaxWithCount)==0:
            self._cachedMaxWithCount.append(self.MaxWithCount(x, 1))
        else:
            curMax = self._cachedMaxWithCount[-1].max
            if x==curMax:
                self._cachedMaxWithCount[-1].count +=1
            elif x > curMax:
                self._cachedMaxWithCount.append(self.MaxWithCount(x, 1))

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        popElement = self._element.pop()
        curMax = self._cachedMaxWithCount[-1].max

        if popElement==curMax:
            self._cachedMaxWithCount[-1].count -= 1
            if self._cachedMaxWithCount[-1].count ==0:
                self._cachedMaxWithCount.pop()
        return popElement


s = Stack1()

s.push(3)
s.push(1)
s.push(2)
s.push(-1)

print s.max()
print s.pop()
print s.pop()
print s.pop()
print s.pop()