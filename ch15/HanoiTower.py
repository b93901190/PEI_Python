
NUM_PEGS = 3

def computeHanoiTower(num_rings):
    def computeHanoiTowerSteps(numRighsTomove, fromPeg, toPeg, usePeg):
        if numRighsTomove > 0:
            computeHanoiTowerSteps(numRighsTomove-1, fromPeg, usePeg, toPeg)
            pegs[toPeg].append(pegs[fromPeg].pop())
            print 'from ', fromPeg, ' to ', toPeg, ' ', [row for row in pegs]
            result.append([fromPeg, toPeg])
            computeHanoiTowerSteps(numRighsTomove-1, usePeg, toPeg, fromPeg)

    result = []
    pegs = [list(reversed(range(1, num_rings+1)))] + [[] for _ in range(1, NUM_PEGS)]
    print [row for row in pegs]
    computeHanoiTowerSteps(num_rings, 0, 1, 2)
    return result

print computeHanoiTower(5)
