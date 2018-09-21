#Custom imports
from mapLoader import mapList
from dinoLoader import dinoList
from map import arkMap

#standard imports
from copy import deepcopy

def makeSpawnEntriesCommandDino(entName, entWeight, dino):
    return makeSpawnEntriesCommand(entName, entryWeight, dino.getID())

def makeSpawnEntriesCommand(entName, entWeight, codeName):
    return "(AnEntryName=\"" + entName + "\",EntryWeight=" + str(entWeight) + ",NPCsToSpawnStrings=(\"" + codeName + "\"))"

def makeSpawnLimitCommandDino(dino, maxPerc):
    return makeSpawnLimitCommand(dino.getID(), maxPerc)

def makeSpawnLimitCommand(codeName, maxPerc):
    return "(NPCClassString=\"" + codeName + "\",MaxPercentageOfDesiredNumToAllow=" + str(maxPerc) + ")"

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

    print("\n\nSpawn Dino Command:\n\n", command)
    return command

"""
Examples:

#ConfigAddNPCSpawnEntriesContainer=
(
    NPCSpawnEntriesContainerClassString="DinoSpawnEntriesSwamp",
    NPCSpawnEntries=
    (
        (AnEntryName="BasilDesert",EntryWeight=0.01,NPCsToSpawnStrings=("Basilisk_Character_BP_C"))
    ),
    NPCSpawnLimits=
    (
        (
            NPCClassString="Basilisk_Character_BP_C",
            MaxPercentageOfDesiredNumToAllow=0.01
        )
    )
)

ConfigAddNPCSpawnEntriesContainer=
(
    NPCSpawnEntriesContainerClassString="DinoSpawnEntriesJungle",
    NPCSpawnEntries=
    (
        (
            AnEntryName="GlowtailIsland",
            EntryWeight=0.1,
            NPCsToSpawnStrings=("LanternLizard_Character_BP_C")
        ),
        (
            AnEntryName="FeatherlightIsland",
            EntryWeight=0.1,
            NPCsToSpawnStrings=("LanternBird_Character_BP_C")
        ),
        (
            AnEntryName="ShinehornIsland",
            EntryWeight=0.1,
            NPCsToSpawnStrings=("LanternGoat_Character_BP_C")
        )
    ),
    NPCSpawnLimits=
    (
        (
            NPCClassString="LanternLizard_Character_BP_C",
            MaxPercentageOfDesiredNumToAllow=0.25
        ),
        (
            NPCClassString="LanternBird_Character_BP_C",
            MaxPercentageOfDesiredNumToAllow=0.25
        ),
        (
            NPCClassString="LanternGoat_Character_BP_C",
            MaxPercentageOfDesiredNumToAllow=0.25
        )
    )
)

"""

#initialize maps
listOfMaps = mapList
listOfDinos = dinoList

print("")
print("-----------------------------------")
print("-----ARK DINO SPAWN GENERATOR-----")
print("-----------------------------------")
print("")

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


#Choose number of dinos to add to region
badInput = True
while(badInput):
    numDinosInputStr = input("Number of dinos to add to this region: ")
    if numDinosInputStr.isnumeric():
        numDinosInput = int(numDinosInputStr)
        badInput = False
    else:
        print("ERROR: Must be a positive whole number")

#Choose dinos
npcSpawnEntryCommands = list()
npcSpawnLimitCommands = list()
for dinoEntry in range(numDinosInput):
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
    entryName = input("Choose a friendly name for this dino (just for reference): ")

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

    #form commands
    entryCommand = makeSpawnEntriesCommandDino(entryName, entryWeight, chosenDino)
    limitCommand = makeSpawnLimitCommandDino(chosenDino, maxPercNumToAllow)

    print("entryCommand: " + entryCommand)
    print("limitCommand: " + limitCommand)

    npcSpawnEntryCommands.append(deepcopy(entryCommand))
    npcSpawnLimitCommands.append(deepcopy(limitCommand))

    if(dinoEntry != numDinosInput-1):
        print("\nNext Dino...\n")

#form final command
generateSpawnDinoCode(chosenRegion, npcSpawnEntryCommands, npcSpawnLimitCommands)

print("\n\nCOPY THE ABOVE LINE INTO YOUR SERVER CODE")
input("Enter any key to end the session...")