from globalConstants import *
from globalVariables import *
from Errors import PositionIncorrect
from handlePlayers import initPlayer, returnNextPlayer

from holes import insertRandomHole, removeOlderHoles



def openFile(modeOpening):
    """
    open the 'save.txt' file
    raise an error if issue
    """
    try:
        saveFile = open("save.txt", mode=modeOpening)
    except IOError:
        saveFile = None
        print("An error was found. Either path is incorrect or file doesn't exist!")
    finally:
        return saveFile

def setBackUp():
    currentPlayer = initPlayer()
    containerDictionnariesKeys = [list(dictionnaryRabbitPLayer1.keys()), list(dictionnaryRabbitPLayer2.keys())]
    indexKeyDictionnary = 0
    isBackUpSucced = True

    saveFile = openFile("w")

    if(saveFile != None):
        # insert Rabbit position
        for dictionnary in containerDictionnaries:
            saveFile.write("Rabbit player" + str(indexKeyDictionnary+1) + ":\n")
            for key, value in dictionnary.items():
                saveFile.write(key + ":" + " " + str(value) + "\n")

            saveFile.write("\n")
            indexKeyDictionnary += 1

        #insert Holes position
        saveFile.write("Holes:\n")
        for hole in listPositionOfHoles:
            saveFile.write(str(hole) + "\n")

        # close the file
        saveFile.close()
    else:
        print("The backup file isn't correct !")



def getBackUp():
    currentPlayer = initPlayer()
    containerDictionnariesKeys = [list(dictionnaryRabbitPLayer1.keys()), list(dictionnaryRabbitPLayer2.keys())]
    indexKeyDictionnary = 0
    isBackUpSucced = True
    isAllPositionRabbitAreGot = False
    listPositionOfHoles.clear()
    removeOlderHoles()
    saveFile = openFile("r")

    if(saveFile != None):
        for line in saveFile:
            listWordsInLine = line.split()

            # rabbit position
            if(isAllPositionRabbitAreGot == False):
                if(len(listWordsInLine) >= 2 and listWordsInLine[0] != "Rabbit"):
                    """
                    listWordsInLine are like:
                        ["A1:", 8]
                        [key of rabbit in dictionnary, position in the board]
                    """
                    try:
                        rabbitPosition = int(listWordsInLine[1])

                        if(rabbitPosition < Board.getFirstElement() or rabbitPosition > NUMBER_OF_CELL): #raise an error if position isn't correct
                            raise PositionIncorrect

                        containerDictionnaries[currentPlayer][containerDictionnariesKeys[currentPlayer][indexKeyDictionnary]] = rabbitPosition #set position in correct dictionnary
                        indexKeyDictionnary += 1
                    except PositionIncorrect:
                        print(listWordsInLine[1], "isn't a correct position for a rabbit in the Board") 

                        isBackUpSucced = False
                        saveFile.close()
                        return isBackUpSucced
                        
                # breakline
                elif(len(listWordsInLine) == 0):
                    # We switch between player
                    currentPlayer = returnNextPlayer(currentPlayer)
                    if(currentPlayer == PLAYER_1): # indicate that we have gotten all rabbit position
                        isAllPositionRabbitAreGot = True

                    indexKeyDictionnary = 0
                    pass

            # holes position
            else:
                # breakline
                if(len(listWordsInLine) > 0 and listWordsInLine[0] != "Holes:"):
                    try:
                        holePosition = int(listWordsInLine[0])

                        if(holePosition < Board.getFirstElement() or holePosition > NUMBER_OF_CELL): #raise an error if position isn't correct
                            raise PositionIncorrect

                        listPositionOfHoles.append(int(listWordsInLine[0]))
                        
                    except PositionIncorrect:
                        isBackUpSucced = False
                        saveFile.close()
                        return isBackUpSucced
        
        saveFile.close()

    else:
        isBackUpSucced = False
        print("The backup file isn't correct !")

    return isBackUpSucced