import random
from globalConstants import NUMBER_OF_CARDS

listOfCards = []

def getCard():
    if(len(listOfCards) > 0):
        return listOfCards.pop()
    else:
        prepareListOfCards()

        return getCard()

def prepareListOfCards():
    initListOfCards()
    shuffleListOfCards()

def initListOfCards():
    for index in range(NUMBER_OF_CARDS):
        # Cards are define between 1 and 4 (see constants.py)
        card = (index%4) + 1
        listOfCards.append(card)

def shuffleListOfCards():
    random.shuffle(listOfCards)



