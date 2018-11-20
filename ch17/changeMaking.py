

def changeMaking(cents):
    COINS = [100, 50, 25, 10, 5, 1]
    numCoins = 0
    for coin in COINS:
        if cents >= coin:
            numCoins += cents // coin
            cents %= coin

    return numCoins

print(changeMaking(20))