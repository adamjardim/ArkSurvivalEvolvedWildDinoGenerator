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

print("Generating Template Configuration for map: ", chosenMap.getName())

templateDinosString = "0,1,5,10,20,30\n"
mapTagString = "#Map\n"
regionTagString = "#Regions\n"

currentFile = open("loadable.txt", "r+")
backupFile = open("backupLoadable.txt", "w+")
backupFile.writelines(currentFile.readlines())

file = open("loadable.txt","w+")

lines = []
lines.append(mapTagString)
lines.append(chosenMap.getName() + "\n\n")
lines.append(regionTagString)

for region in chosenMap.getListOfRegions(): 
    #print("\t", regionCounter, " - ", region)
    lines.append("= " + region + "\n")
    lines.append("(" + str(entryWeight) + "," + str(maxPercNumToAllow) + ")\n")
    lines.append(templateDinosString)

file.writelines(lines)
