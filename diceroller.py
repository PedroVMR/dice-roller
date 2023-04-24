from random import randint

def diceRoller(amount, dicetype):
    diceList = []
    for dice in range(amount):
        dice = randint(1, dicetype)
        diceList.append(dice)
    return diceList

amountDices, diceType = input("Digite a quantidade de dados e o tipo de dado no formato 'XdY', onde X é a quantidade e Y é o tipo: ").split("d")
diceList = diceRoller(int(amountDices), int(diceType))

total = 0
for dice in diceList:
    total += dice
print(f"{total} <= {diceList} {amountDices}d{diceType}")