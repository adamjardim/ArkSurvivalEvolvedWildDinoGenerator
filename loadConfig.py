#Custom imports
from mapLoader import mapList
from dinoLoader import dinoList
from dinoCodeGeneratorUtility import generateSpawnDinoCode, makeSpawnEntriesCommandDino, makeSpawnLimitCommandDino, autoname, templateFindGlobalEntryWeight, templateFindGlobalMaxPerc, templateFindMap, templateFindDinos, notifyError
from map import arkMap
from configuration import configuration, regionConfiguration

#standard imports
from copy import deepcopy
import re
import os
import sys

#initialize maps
listOfMaps = mapList
listOfDinos = dinoList

print("\n\n\n")

config = open("loadable.txt", "r")
#contents = config.read()
#print(contents)

#Find map
mapString = ""
lines = config.readlines()
mapLine = 0
for x in range(0,len(lines)):
    #print("[",mapLine,"]: ",lines[x])
    if "#Map" in lines[x]:
        mapString = lines[x+1]
        break
    mapLine = mapLine + 1
if mapString == "":
    print("Didn't find #Map tag")
    input("Enter any key to end the session...")
    sys.exit()
mapString = mapString.strip("\n")
chosenMap = listOfMaps[0]
foundMatchingMap = False
for m in mapList:
    if mapString == m.getName():
        foundMatchingMap = True
        chosenMap = m
        break
if not foundMatchingMap:
    print("Didn't find a matching map with name: \"", mapString, "\"")
    input("Enter any key to end the session...")
    sys.exit()

config = configuration(chosenMap)

commands = []
#find regions
foundRegions = False
regionLine = mapLine
for x in range(mapLine,len(lines)):
    #print("[",regionLine,"]: ",lines[x])
    if "#Regions" in lines[x]:
        foundRegions = True
    regionLine = regionLine + 1
if not foundRegions:
    print("Didn't find #Regions tag")
    input("Enter any key to end the session...")
    sys.exit()

regionIndex = 0
for x in range(0,len(lines)):
    if "= " in lines[x]:
        regionName = lines[x].split('= ')[1].split('\n')[0]
        regions = chosenMap.getListOfRegions()
        foundMatchingRegion = False
        for region in regions:
            if regionName == region:
                foundMatchingRegion = True
                chosenRegion = region
                #print("Found Region: ", chosenRegion)
        if not foundMatchingRegion:
            print("Found a region that doesn't match given map: \"", regionName, "\"")
            input("Enter any key to end the session...")
            sys.exit()
        print("Region #", regionIndex)
        regConfig = regionConfiguration(chosenRegion)
        weightLinefirst = lines[x+1].split('(')[1]
        weightLine = weightLinefirst.split(')')[0]
        entryWeight = weightLine.split(',')[0]
        regConfig.setEntryWeight(float(entryWeight))
        maxPercNumToAllow = weightLine.split(',')[1]
        regConfig.setMax(float(maxPercNumToAllow))
        dinoList = lines[x+2].split(',')
        npcSpawnEntryCommands = list()
        npcSpawnLimitCommands = list()
        for dino in dinoList:
            chosenDino = listOfDinos[int(dino)]
            regConfig.addDino(int(dino))
            entryName = autoname(chosenDino,regionName)
            #form commands
            entryCommand = makeSpawnEntriesCommandDino(entryName, entryWeight, chosenDino)
            limitCommand = makeSpawnLimitCommandDino(chosenDino, maxPercNumToAllow)
            npcSpawnEntryCommands.append(deepcopy(entryCommand))
            npcSpawnLimitCommands.append(deepcopy(limitCommand))
        command = generateSpawnDinoCode(chosenRegion, npcSpawnEntryCommands, npcSpawnLimitCommands)
        commands.append(command)
        commands.append("\n")
        regionIndex = regionIndex + 1

# double check with user
badConfig = False
isCorrect = "Fart"
while (isCorrect != "y") and (isCorrect != "n"):
    isCorrect = input("Is this correct? (y/n): ")
    if (isCorrect != "y") and (isCorrect != "n"):
            print("Please enter 'y' or 'n'")
    if isCorrect == "n":
        badConfig = True
        break

if not badConfig:
    currentFile = open("generatedCode.txt", "r+")
    backupFile = open("backupGeneratedCode.txt", "w+")
    backupFile.writelines(currentFile.readlines())
    print("Generating code...")
    outFile = open("generatedCode.txt", "w+")
    outFile.writelines(commands)
else:
    print("Please correct your configuration document")
        
input("Enter any key to end the session...")
