from globalConstants import *

"""
Those dictrionnaries will saved the place
& the state of all rabbits
"""
dictionnaryRabbitPLayer1 = {
    "A1": BEGIN,
    "B1" : BEGIN, 
    "C1": BEGIN, 
    "D1": BEGIN 
}
dictionnaryRabbitPLayer2 = {
    "A2": BEGIN,
    "B2" : BEGIN, 
    "C2": BEGIN, 
    "D2": BEGIN 
}

# use to loop over the 2 dictionnary
containerDictionnaries = [dictionnaryRabbitPLayer1, dictionnaryRabbitPLayer2]

# board to contain rabbits / holes / free places
board = [0 for i in range (NUMBER_OF_CELL)]