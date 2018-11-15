import collections

def isRansomNote(letter, magazine):
    letterTable = collections.Counter(letter)

    for c in magazine:
        if c in letterTable:
            letterTable[c] -= 1
            if letterTable[c]==0:
                del letterTable[c]
                if not letterTable:
                    return True

    return not letterTable

def isRansomNotePythonic(letter, magazine):
    return (not collections.Counter(letter) - collections.Counter(magazine))

