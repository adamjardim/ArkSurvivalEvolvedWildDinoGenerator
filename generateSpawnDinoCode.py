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
    command = "ConfigAddNPCSpawnEntriesContainer=(NPCSpawnEntriesContainerClassString=\"" + reg + ",NPCSpawnEntries=("

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
mapChoiceInput = int(input("Choose a map #: "))
chosenMap = listOfMaps[mapChoiceInput]
print("You chose : ", chosenMap.getName(), "\n")

#Choose a region
print("Region Choices:")
regionCounter = 0
for region in chosenMap.getListOfRegions():
    print("\t", regionCounter, " - ", region)
    regionCounter+=1
regionChoiceInput = int(input("Choose a region #: "))
chosenRegion = chosenMap.getListOfRegions()[regionChoiceInput]
print("You chose : ", chosenRegion, "\n")

#Choose number of dinos to add to region
numDinosInput = int(input("Number of dinos to add to this region: "))

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
    chosenDinoInput = int(input("Which dino would you like to add? : "))
    chosenDino = listOfDinos[chosenDinoInput]
    print("You chose : ", chosenDino.getName())

    #choose friendly name
    entryName = input("Choose a friendly name for this dino (just for reference): ")

    #choose entry weight
    entryWeight = 999
    while((entryWeight > 1) or (entryWeight < 0)):
        entryWeight = float(input("Entry Weight: "))
        if((entryWeight > 1) or (entryWeight < 0)):
            print("ERROR: Entry Weight must be between 0 and 1")

    #choose max percent
    maxPercNumToAllow = 999
    while((maxPercNumToAllow > 1) or (maxPercNumToAllow < 0)):
        maxPercNumToAllow = float(input("MaxPercentageOfDesiredNumToAllow: "))
        if((maxPercNumToAllow > 1) or (maxPercNumToAllow < 0)):
            print("ERROR: MaxPercentageOfDesiredNumToAllow must be between 0 and 1")

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