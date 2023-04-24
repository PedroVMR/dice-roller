from random import randint

def diceRoller(amount, dicetype):
    diceList = []
    for dice in range(amount):
        dice = randint(1, dicetype)
        diceList.append(dice)
    return diceList

amountDices, diceType = input("Enter the amount of dices and the dice type in 'XdY' format, where X is the amount and Y is the type: ").split("d")
diceList = diceRoller(int(amountDices), int(diceType))

total = 0
for dice in diceList:
    total += dice
print(f"{total} <= {diceList} {amountDices}d{diceType}")
