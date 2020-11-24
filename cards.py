import random
from globalConstants import NUMBER_OF_CARDS

listOfCards = []

def getCard():
    """
    Return 1 card on the deck
    Prepare the deck if is empty
    """
    if(len(listOfCards) > 0):
        return listOfCards.pop()
    else:
        prepareListOfCards()

        return getCard()

def prepareListOfCards():
    initListOfCards()
    shuffleListOfCards()

def initListOfCards():
    """
    Append all different cards on the deck
    However the deck is sorted at this point
    """
    for index in range(NUMBER_OF_CARDS):
        # Cards are define between 1 and 4 (see constants.py)
        card = (index%4) + 1
        listOfCards.append(card)

def shuffleListOfCards():
    """
    Mixed up the deck
    """
    random.shuffle(listOfCards)



