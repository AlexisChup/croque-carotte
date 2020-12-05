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
            saveFile.write(DICO_PLAYER_NAME[indexKeyDictionnary] + "\n")
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
    indexLine = 1

    if(saveFile != None):
        for line in saveFile:
            listWordsInLine = line.split()

            # rabbit position
            if(isAllPositionRabbitAreGot == False):
                # breakline
                if(indexLine == 6 or indexLine == 12):
                    # We switch between player
                    currentPlayer = returnNextPlayer(currentPlayer)
                    if(currentPlayer == PLAYER_1): # indicate that we have gotten all rabbit position
                        isAllPositionRabbitAreGot = True

                    indexKeyDictionnary = 0
                    
                elif(indexLine == 1 or indexLine == 7): #it's the name of the player
                    """
                    listWordsInLine are like:
                        "JOUEUR 1"
                    """
                    namePlayer = ""
                    for word in listWordsInLine:
                        namePlayer += (" " +word)

                    DICO_PLAYER_NAME[currentPlayer] = namePlayer
                else:
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
                        


            # holes position
            else:
                # breakline
                if(indexLine != 13):
                    try:
                        holePosition = int(listWordsInLine[0])

                        if(holePosition < Board.getFirstElement() or holePosition > NUMBER_OF_CELL): #raise an error if position isn't correct
                            raise PositionIncorrect

                        listPositionOfHoles.append(int(listWordsInLine[0]))
                        
                    except PositionIncorrect:
                        isBackUpSucced = False
                        saveFile.close()
                        return isBackUpSucced

            indexLine += 1
        
        saveFile.close()

    else:
        isBackUpSucced = False
        print("The backup file isn't correct !")

    return isBackUpSucced