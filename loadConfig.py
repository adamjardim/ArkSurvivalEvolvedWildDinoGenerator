#Custom imports
from mapLoader import mapList
from dinoLoader import dinoList
from dinoCodeGeneratorUtility import generateSpawnDinoCode, makeSpawnEntriesCommandDino, makeSpawnLimitCommandDino, autoname, templateFindGlobalEntryWeight, templateFindGlobalMaxPerc, templateFindMap, templateFindDinos, notifyError
from map import arkMap

#standard imports
from copy import deepcopy
import re
import os
import sys

#initialize maps
listOfMaps = mapList
listOfDinos = dinoList

currentFile = open("generatedCode.txt", "r+")
backupFile = open("backupGeneratedCode.txt", "w+")
backupFile.writelines(currentFile.readlines())

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

for x in range(regionLine,len(lines)):
    if foundRegions:
        if "=" in lines[x]:
            regionName = lines[x].split('= ')[1].split('\n')[0]

            regions = chosenMap.getListOfRegions()
            foundMatchingRegion = False
            for region in regions:
                if regionName == region:
                    foundMatchingRegion = True
                    chosenRegion = region
            if not foundMatchingRegion:
                print("Found a region that doesn't match given map: \"", regionName, "\"")
                input("Enter any key to end the session...")
                sys.exit()
            weightLinefirst = lines[x+1].split('(')[1]
            print(weightLinefirst)
            weightLine = weightLinefirst.split(')')[0]
            print(weightLine)
            entryWeight = weightLine.split(',')[0]
            maxPercNumToAllow = weightLine.split(',')[1]
            dinoList = lines[x+2].split(',')
            npcSpawnEntryCommands = list()
            npcSpawnLimitCommands = list()
            for dino in dinoList:
                chosenDino = listOfDinos[int(dino)]
                entryName = autoname(chosenDino,regionName)
                #form commands
                entryCommand = makeSpawnEntriesCommandDino(entryName, entryWeight, chosenDino)
                limitCommand = makeSpawnLimitCommandDino(chosenDino, maxPercNumToAllow)
                npcSpawnEntryCommands.append(deepcopy(entryCommand))
                npcSpawnLimitCommands.append(deepcopy(limitCommand))
            command = generateSpawnDinoCode(chosenRegion, npcSpawnEntryCommands, npcSpawnLimitCommands)
            commands.append(command)
            commands.append("\n")

print("Generating code...")
outFile = open("generatedCode.txt", "w+")
outFile.writelines(commands)
input("Enter any key to end the session...")