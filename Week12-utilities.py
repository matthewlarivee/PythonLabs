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

def Union(list1, list2):
    finalList = []
    for i in range(len(list1)):
        if(list1[i] not in finalList):
            finalList.append(list1[i])
    for j in range(len(list2)):
        if(list2[j] not in finalList):
            finalList.append(list2[j])
    return finalList

def Intersection(list1, list2):
    unionList = []
    intersectionList = []
    for i in range(len(list1)):
        if(list1[i] not in unionList):
            unionList.append(list1[i])
        else:
            intersectionList.append(list1[i])
    for j in range(len(list2)):
        if(list2[j] not in unionList):
            unionList.append(list2[j])
        else:
            intersectionList.append(list2[j])
    return intersectionList
