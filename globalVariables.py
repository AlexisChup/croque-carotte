from globalConstants import *

dictionnaryRabbitPLayer1 = {
    "A1": BEGIN,
    "B1" : BEGIN , 
    "C1": BEGIN , 
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

board = [0 for i in range (NUMBER_OF_CELL)]