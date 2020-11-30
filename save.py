from globalConstants import *
from globalVariables import *

try:
    saveFile = open("save.txt", mode="r")
except IOError:
    saveFile = ""
    print("An error was found. Either path is incorrect or file doesn't exist!")

for line in saveFile:
    words = line.split()
    if(len(words) >= 2 and words[0] != "Rabbit"):
        rabbitState = words[1]
        print("rabbitState:", rabbitState)

    # for word in words:
    #     print("word_ ", word, end=" ", sep="")

    print("")