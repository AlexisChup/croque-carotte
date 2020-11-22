from Errors import ValueNotInInterval

def handleInputRabbitNumero(numberOfRabbitAlive):
    isInputCorrect = False
    inputNumeroOfRabbit = None

    while(not isInputCorrect):
        try:
            inputNumeroOfRabbit = input("Saisir le numéro du lapin à avancer : ")

            # this if is used to be faster in the game
            # by default, if the user press [ENTER], the rabbit number will be 1
            if(inputNumeroOfRabbit == ""):
                isInputCorrect = True
                inputNumeroOfRabbit = 1
            
            inputNumeroOfRabbit = int(inputNumeroOfRabbit)

            if(inputNumeroOfRabbit >= 1 and inputNumeroOfRabbit <= numberOfRabbitAlive):
                isInputCorrect = True

            elif(inputNumeroOfRabbit < 1 or inputNumeroOfRabbit > numberOfRabbitAlive):
                raise ValueNotInInterval

        except ValueError:
            print("Oops! Ce n'était pas un nombre.  Réessayez...")
            
        except ValueNotInInterval:
            print("Oops! Ce n'était pas un nombre compris entre 1 et", numberOfRabbitAlive, "inclus.  Réessayez...")

    return (inputNumeroOfRabbit - 1) # -1 because array start at 0

def handleInputPlayerAction():
    playerAction = input()

    return False if (playerAction == 'q') else True




