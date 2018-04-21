# MinimumNumberOfCoinsNeeded Implementation

import sys

def openFile(fileName):
    money = ""
    coinDenominations = []
    with open(fileName) as f:
        money = f.readline().rstrip("\n")
        coinDenominations = f.readline().rstrip("\n").split(",")
    if not coinDenominations or money == "":
        return 1
    return money, coinDenominations

def dpChange(money,coins):
    money = int(money)
    minNumCoins = [0]
    for m in range(1,money+1):
        minNumCoins.append(sys.maxsize)
        for i in coins:
            i = int(i)
            if m >= i:
                if minNumCoins[m-i]+1 < minNumCoins[m]:
                    minNumCoins[m] = minNumCoins[m-i]+1
    print("minNumCoins:\n" + " ".join(str(x) for x in minNumCoins))
    return minNumCoins[money]

money, coinDenominations = openFile("./data/Rosalind_data_p36.txt")
# print("money:\n" + str(money))
print("coin denominations:\n" + " ".join(coinDenominations))
minNumCoins = dpChange(money, coinDenominations)
print("The Minimum Number of Coins Needed to make " + str(money) + " is:\n" + str(minNumCoins))