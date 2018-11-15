
import collections

def findAnagrams(dictionary):
    sortedStrToAnagrams = collections.defaultdict(list)

    for s in dictionary:
        sortedStrToAnagrams[''.join(sorted(s))].append(s)

    return [ group for group in sortedStrToAnagrams.values() if len(group) >= 2]

dictionary = 'debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money'

print findAnagrams(dictionary)
