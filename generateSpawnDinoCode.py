#Custom imports
from mapLoader import mapList
from dinoLoader import dinoList
from dinoCodeGeneratorUtility import generateSpawnDinoCode, makeSpawnEntriesCommandDino, makeSpawnLimitCommandDino, autoname
from map import arkMap

#standard imports
from copy import deepcopy

#initialize maps
listOfMaps = mapList
listOfDinos = dinoList

#initialize settings
useGlobalWeightAndPercent = True
useColumns = True

print("")
print("-----------------------------------")
print("-----ARK DINO SPAWN GENERATOR-----")
print("-----------------------------------")
print("")
maxListHeight = 50
#Choose a map
print("Map Choices:")
mapCounter = 0
for map in listOfMaps:
    print("\t", mapCounter, " - ", map.getName())
    mapCounter+=1
badMapInput = True
while(badMapInput):
    mapChoiceInputStr = input("Choose a map #: ")
    if mapChoiceInputStr.isnumeric():
        mapChoiceInput = int(mapChoiceInputStr)
        if (mapChoiceInput >= 0) and (mapChoiceInput < len(listOfMaps)):
            badMapInput = False
        else:
            print("ERROR: Map choice number must be one listed above!")
    else:
        print("ERROR: Map choice must be a number!")

chosenMap = listOfMaps[mapChoiceInput]
print("You chose : ", chosenMap.getName(), "\n")

#Choose a region
print("Region Choices:")
regionCounter = 0
for region in chosenMap.getListOfRegions(): 
    print("\t", regionCounter, " - ", region)
    regionCounter+=1
badRegionInput = True
while(badRegionInput):
    regionChoiceInputStr = input("Choose a region #: ")
    if (regionChoiceInputStr.isnumeric()):
        regionChoiceInput = int(regionChoiceInputStr)
        if regionChoiceInput >= 0 and regionChoiceInput < len(chosenMap.getListOfRegions()):
            badRegionInput = False
        else:
            print("ERROR: Region choice number must be one listed above!")
    else:
        print("ERROR: Region choice must be a number!")

chosenRegion = chosenMap.getListOfRegions()[regionChoiceInput]
print("You chose : ", chosenRegion, "\n")

#get global settings if selected
if useGlobalWeightAndPercent:
    entryWeight = 999
    while((entryWeight > 1) or (entryWeight < 0)):
        entryWeightStr = input("Global Entry Weight: ")
        if (entryWeightStr.replace('.','',1).isnumeric()):
            entryWeight = float(entryWeightStr)
            if((entryWeight > 1) or (entryWeight < 0)):
                print("ERROR: Entry Weight must be between 0 and 1")
        else:
                print("Entry weight must be a number")
    maxPercNumToAllow = 999
    while((maxPercNumToAllow > 1) or (maxPercNumToAllow < 0)):
        maxPercNumToAllowStr = input("Global MaxPercentageOfDesiredNumToAllow: ")
        if (maxPercNumToAllowStr.replace('.','',1).isnumeric()):
            maxPercNumToAllow = float(maxPercNumToAllowStr)
            if((maxPercNumToAllow > 1) or (maxPercNumToAllow < 0)):
                print("ERROR: MaxPercentageOfDesiredNumToAllow must be between 0 and 1")
        else:
            print("Max percent must be a number")

'''
#Choose number of dinos to add to region
badInput = True
while(badInput):
    numDinosInputStr = input("Number of dinos to add to this region: ")
    if numDinosInputStr.isnumeric():
        numDinosInput = int(numDinosInputStr)
        badInput = False
    else:
        print("ERROR: Must be a positive whole number")
'''

#Choose dinos
npcSpawnEntryCommands = list()
npcSpawnLimitCommands = list()
moreDinos = True
while moreDinos:
    #choose dino
    print("Dino Choices: ")
    dinoCounter = 0
    for dino in listOfDinos:
        print("\t", dinoCounter, " - ", listOfDinos[dinoCounter].getName())
        dinoCounter+=1
    badDinoInput = True
    while(badDinoInput):
        chosenDinoInputStr = input("Choose a dino #: ")
        if (chosenDinoInputStr.isnumeric()):
            chosenDinoInput = int(chosenDinoInputStr)
            if (chosenDinoInput >= 0) and (chosenDinoInput < len(listOfDinos)):
                badDinoInput = False
            else:
                print("ERROR: Dino choice number must be one listed above!")
        else:
            print("ERROR: Dino choice must be a number!")
    chosenDino = listOfDinos[chosenDinoInput]
    print("You chose : ", chosenDino.getName())

    #choose friendly name
    entryName = autoname(chosenDino, chosenRegion)

    if not useGlobalWeightAndPercent:
        #choose entry weight
        entryWeight = 999
        while((entryWeight > 1) or (entryWeight < 0)):
            entryWeightStr = input("Entry Weight: ")
            if (entryWeightStr.replace('.','',1).isnumeric()):
                entryWeight = float(entryWeightStr)
                if((entryWeight > 1) or (entryWeight < 0)):
                    print("ERROR: Entry Weight must be between 0 and 1")
            else:
                print("Entry weight must be a number")

        #choose max percent
        maxPercNumToAllow = 999
        while((maxPercNumToAllow > 1) or (maxPercNumToAllow < 0)):
            maxPercNumToAllowStr = input("MaxPercentageOfDesiredNumToAllow: ")
            if (maxPercNumToAllowStr.replace('.','',1).isnumeric()):
                maxPercNumToAllow = float(maxPercNumToAllowStr)
                if((maxPercNumToAllow > 1) or (maxPercNumToAllow < 0)):
                    print("ERROR: MaxPercentageOfDesiredNumToAllow must be between 0 and 1")
            else:
                print("Max percent must be a number")

    print("You chose ", chosenDino.getName(), " : Entry Weight: " , entryWeight , " : Max Percent: ", maxPercNumToAllow)
    isCorrect = "fart"
    while (isCorrect != "y") and (isCorrect != "n"):
        isCorrect = input("Is this correct? (y/n): ")
        if (isCorrect != "y") and (isCorrect != "n"):
            print("Please enter 'y' or 'n'")
    if isCorrect == "n":
        continue

    #form commands
    entryCommand = makeSpawnEntriesCommandDino(entryName, entryWeight, chosenDino)
    limitCommand = makeSpawnLimitCommandDino(chosenDino, maxPercNumToAllow)

    print("entryCommand: " + entryCommand)
    print("limitCommand: " + limitCommand)

    npcSpawnEntryCommands.append(deepcopy(entryCommand))
    npcSpawnLimitCommands.append(deepcopy(limitCommand))

    moreDinoString = "fart"
    while (moreDinoString != "y") and (moreDinoString != "n"):
        moreDinoString = input("Would you like to add another dino? (y/n): ")
        if (moreDinoString != "y") and (moreDinoString != "n"):
            print("Please enter 'y' or 'n'")
    if moreDinoString == "y":
        print("Next dino...")
    if moreDinoString == "n":
        moreDinos = False

#form final command
generateSpawnDinoCode(chosenRegion, npcSpawnEntryCommands, npcSpawnLimitCommands)

print("\n\nCOPY THE ABOVE LINE INTO YOUR SERVER CODE")
input("Enter any key to end the session...")