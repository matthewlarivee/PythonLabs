#   Matthew Larivee
#   CSCI 102 – Section A
#   Week 12 - Part A

def PrintOutput(output):
    print("OUTPUT %s" %(output))

def LoadFile(fileName):
    f = open(fileName,"r")
    contents = f.read()
    f.close()
    finalList = contents.split("\n")
    return finalList

