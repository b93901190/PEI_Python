
def numCombinations(finalScore, scoresPerPlay):
    numCombiationsForScores = [[1] + [0]*finalScore for _ in scoresPerPlay]

    for i in range(len(scoresPerPlay)):
        for j in range(1, finalScore+1):
            withoutThisPlay = (numCombiationsForScores[i-1][j] if i>0 else 0)
            withThisPlay = (numCombiationsForScores[i][j - scoresPerPlay[i]] if j >= scoresPerPlay[i] else 0)
            numCombiationsForScores[i][j] = withoutThisPlay + withThisPlay

    return numCombiationsForScores[-1][-1]

print(numCombinations(15, [2, 3,7]))
