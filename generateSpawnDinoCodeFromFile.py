#Custom imports
from mapLoader import mapList
from dinoLoader import dinoList
from dinoCodeGeneratorUtility import generateSpawnDinoCode, makeSpawnEntriesCommandDino, makeSpawnLimitCommandDino, autoname, templateFindGlobalEntryWeight, templateFindGlobalMaxPerc, templateFindMap, templateFindDinos, notifyError
from map import arkMap

#standard imports
from copy import deepcopy
import re
import os

#initialize maps
listOfMaps = mapList
listOfDinos = dinoList

#initialize command lists
npcSpawnEntryCommands = list()
npcSpawnLimitCommands = list()

#get the file
user_input = "template.txt"
assert os.path.exists(user_input), "I did not find the file at: "+str(user_input)
f = open(user_input,'r+')
content = [line.rstrip('\n') for line in f]

entryWeight = templateFindGlobalEntryWeight(content)
if entryWeight == "ERROR":
    notifyError()
maxPerc = templateFindGlobalMaxPerc(content)
if maxPerc == "ERROR":
    notifyError()
mapChoiceStr = templateFindMap(content)
if int(mapChoiceStr) >= len(listOfMaps):
    print("Map choice must be between 0 and ", len(listOfMaps)-1)
    notifyError()
dinoChoices = templateFindDinos(content)
for ecosystem in dinoChoices:
    items = ecosystem.split()
    regionStr = items[0]
    mapChoice = listOfMaps[int(mapChoiceStr)]
    if int(regionStr) >= len(mapChoice.getListOfRegions()):
        print("ERROR detected in #dino line: ", ecosystem)
        print("Region must be between 0 and ", len(mapChoice.getListOfRegions())-1)
        notifyError()
    chosenRegion = mapChoice.getListOfRegions()[int(regionStr)]
    print("Region: ", chosenRegion)
    dinos = items[0:]
    for dino in dinos:
        if int(dino) > len(dinoList):
            print("ERROR detected in #dino line: ", ecosystem)
            print("ERROR Dino choice is invalid: ", dino)
            notifyError()
        chosenDino = dinoList[int(dino)]
        print("\t ", int(dino)," : ", chosenDino.getName())

        #choose friendly name
        entryName = autoname(chosenDino, chosenRegion)
        
        #form commands
        entryCommand = makeSpawnEntriesCommandDino(entryName, entryWeight, chosenDino)
        limitCommand = makeSpawnLimitCommandDino(chosenDino, maxPerc)

        npcSpawnEntryCommands.append(deepcopy(entryCommand))
        npcSpawnLimitCommands.append(deepcopy(limitCommand))

#form final command
generateSpawnDinoCode(chosenRegion, npcSpawnEntryCommands, npcSpawnLimitCommands)

print("\n\nCOPY THE ABOVE LINE INTO YOUR SERVER CODE")
input("Enter any key to end the session...")



    
    
    
