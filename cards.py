import random
from constants import *

listOfCards = []

def initListOfCards():
    for index in range(NUMBER_OF_CARDS):
        # Cards are define between 1 and 4 (see constants.py)
        card = (index%4) + 1
        listOfCards.append(card)

def shuffleListOfCards():
    random.shuffle(listOfCards)

def prepareListOfCards():
    initListOfCards()
    shuffleListOfCards()

def getCard():
    if(len(listOfCards) > 0):
        return listOfCards.pop()
    else:
        prepareListOfCards()

        return getCard()