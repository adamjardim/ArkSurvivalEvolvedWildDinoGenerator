import sys
from dinoLoader import dinoList

def notifyError():
    input("There was an error! Press any key to end the session...")
    sys.exit()

def templateFindGlobalEntryWeight(lines):
    foundMark = False
    for line in lines:
        if foundMark:
            print("Found Entry Weight: ", line)
            if float(line) < 0 or float(line) > 1:
                print("ERROR: Entry Weight must be between 0 and 1")
                return "ERROR"
            return line
        if(not line.find("#global entry weight")):
            foundMark = True
            continue
    if foundMark == False:
        print("Unable to find global entry weight!")
        return "ERROR"

def templateFindGlobalMaxPerc(lines):
    foundMark = False
    for line in lines:
        if foundMark:
            print("Found Max Percent: ", line)
            if float(line) < 0 or float(line) > 1:
                print("ERROR: Max Percentage must be between 0 and 1")
                return "ERROR"
            return line
        if(not line.find("#global max percent")):
            foundMark = True
            continue
    if foundMark == False:
        print("Unable to find global max percent!")
        return "ERROR"

def templateFindMap(lines):
    foundMark = False
    for line in lines:
        if foundMark:
            print("Found Map: ", line)
            return line
        if(not line.find("#map")):
            foundMark = True
            continue
    if foundMark == False:
        print("Unable to find map!")
        return "ERROR"

def templateFindDinos(lines):
    foundMark = False
    dinoInventory = []
    for line in lines:
        if(not line.find("#dinos")):
            foundMark = True
            continue
        if (foundMark) and (not line.find("===")):
            break
        if foundMark:
            if len(line) < 2:
                continue
            dinoList.append(line)
    if foundMark == False:
        print("Unable to find dinos!")
        return "ERROR"
    print(dinoInventory)
    return dinoInventory

def makeSpawnEntriesCommandDino(entName, entWeight, dino):
    return makeSpawnEntriesCommand(entName, entWeight, dino.getID())

def makeSpawnEntriesCommand(entName, entWeight, codeName):
    return "(AnEntryName=\"" + entName + "\",EntryWeight=" + str(entWeight) + ",NPCsToSpawnStrings=(\"" + codeName + "\"))"

def makeSpawnLimitCommandDino(dino, maxPerc):
    return makeSpawnLimitCommand(dino.getID(), maxPerc)

def makeSpawnLimitCommand(codeName, maxPerc):
    return "(NPCClassString=\"" + codeName + "\",MaxPercentageOfDesiredNumToAllow=" + str(maxPerc) + ")"

def autoname(dino, reg):
    return dino.getID() + "_" + reg

def generateSpawnDinoCode(reg, listOfSpawnEntryCommands, listOfSpawnLimitCommands):
    command = "ConfigAddNPCSpawnEntriesContainer=(NPCSpawnEntriesContainerClassString=\"" + reg + "\",NPCSpawnEntries=("

    #add spawn entry commands
    for index in range(len(listOfSpawnEntryCommands)):
        command+=listOfSpawnEntryCommands[index]
        if (index != len(listOfSpawnEntryCommands)-1):
            command+=","
    command+="),NPCSpawnLimits=("

    #add spawn limit commands
    for index in range(len(listOfSpawnLimitCommands)):
        command+=listOfSpawnLimitCommands[index]
        if (index != len(listOfSpawnLimitCommands)-1):
            command+=","

    command+="))"

    file = open('GeneratedCode.txt', 'w+')
    file.write(command)

    #print("\n\nSpawn Dino Command:\n\n", command)
    return command

def getDinoNames(dinos):
    activeList = []
    for index in range(len(dinos)):
        activeList.append(dinos[index].getName())
    return activeList

def printDinoNamesOnNewLines(dinos):
    nameList = getDinoNames(dinos)
    if len(dinos) == 0:
        print("[DINO LIST IS EMPTY]")
        return
    for name in nameList:
        print(name)

def getDinoListWithLettersAnywhere(word):
    activeList = []
    for index in range(len(dinoList)):
        if word in dinoList[index].getName():
            activeList.append(dinoList[index])
    return activeList

def getDinoListWithLettersStart(word):
    activeList = []
    for index in range(len(dinoList)):
        if dinoList[index].getName().startswith(word):
            activeList.append(dinoList[index])
    return activeList

#print("==============================")
#print("========UTILITY TESTER========")
#print("==============================")
#wordToSearch = input("Search Term : ")
#print("\nRESULTS:\n")
#rintDinoNamesOnNewLines(getDinoListWithLettersAnywhere(wordToSearch))
#print("\nEND OF RESULTS\n")