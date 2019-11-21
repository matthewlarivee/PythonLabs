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

def UpdateString(stringy, insert, number):
    strList = []
    for i in range(len(stringy)):
        strList.append(stringy[i])
    strList[number] = insert
    strList = ''.join(strList)
    print("OUTPUT %s" %(strList))

def FindWordCount(listy, word):
    counter = 0
    for i in range(len(listy)):
        counter = counter + listy[i].count(word)
    return counter

def ScoreFinder(playerList, scoreList, player):
    for i in range(len(playerList)):
        playerList[i] = playerList[i].lower()
    if(player.lower() not in playerList):
        PrintOutput("player not found")
    else:
        PrintOutput("%s got a score of %d" %(player, scoreList[playerList.index(player.lower())]))
