from tkinter import *
import dinoCodeGeneratorUtility
from dinoLoader import dinoList
from mapLoader import mapList

regionDinoMap = {}
def addToDinoMap(regionToAdd, dinoToAdd):
    if regionDinoMap.has_key(regionToAdd):
        dinosInRegion = regionDinoMap[regionToAdd]
        if not dinoToAdd in dinosInRegion:
            dinosInRegion.append(dinoToAdd)
        regionDinoMap[regionToAdd] = dinosInRegion
    else:
        regionDinoMap[regionToAdd] = []
        regionDinoMap[regionToAdd].append(dinoToAdd)

def removeDinoFromMap(regionToRemove,dinoToRemove):
    if regionDinoMap.has_key(regionToRemove):
        dinosInRegion = regionDinoMap[regionToRemove]
        if dinoToRemove in dinosInRegion:
            dinosInRegion.pop(dinoToRemove)
        regionDinoMap[regionToRemove] = dinosInRegion
    if len(regionDinoMap[regionToRemove]) == 0:
        regionDinoMap.pop(regionToRemove)

def generateDinoMapFrame(parent, inputRegion):
    dinosInThisRegionLabel = Label(parent, text="Dinos in this region:")
    dinosInThisRegionLabel.pack()
    if regionDinoMap.has_key(inputRegion):
        for regionDino in regionDinoMap:
            def removeDinoCallback(*args):
                removeDinoFromMap(inputRegion,regionDino)
            Button(parent, text=regionDino.getName(), command=removeDinoCallback)
            Button.pack()
    else:
        noDinosWarning = Label(parent, text="No Dinos in region")
        noDinosWarning.pack()


top = Tk()
top.geometry("1000x1000")
top.title("Ark Dino Code Generator")

introText = Label(top, text="Welcome to the Ark Dino Code Generator.")
introText.pack()

#CHOOSE A MAP
mapChooseText = Label(top, text="Choose a map:")
mapChooseText.pack()

mapChoiceNames = []
for mapChoice in mapList:
    mapChoiceNames.append(mapChoice.getName())
mapChoiceVariable = StringVar(top)
mapChoiceVariable.set("---")
mapChoiceDropdownMenu = OptionMenu(top, mapChoiceVariable, *mapChoiceNames)
mapChoiceDropdownMenu.config(width=90, font=('Helvetica', 12))
mapChoiceDropdownMenu.pack()

selectedMapChoice = Label(text="", font=('Helvetica', 12), fg='black')
selectedMapChoice.pack()
selectedIndex = 0
chosenMap = mapList[selectedIndex]
def mapDropdownCallback(*args):
    selectedMapChoice.configure(text="The selected item is {}".format(mapChoiceVariable.get()))
    for index in range(len(mapList)):
        if (mapChoiceVariable.get() == mapList[index].getName()):
            selectedIndex = index
            break
    chosenMap = mapList[selectedIndex]
mapChoiceVariable.trace("w", mapDropdownCallback)

#CHOOSE A REGION
regionChooseText = Label(top, text="Choose a region to add:")
regionChooseText.pack()

regionFrame = Frame(top)
regionChoiceNames = chosenMap.getListOfRegions();
regionChoiceVariable = StringVar(regionFrame)
regionChoiceVariable.set("---")
regionChoiceDropdownMenu = OptionMenu(regionFrame, regionChoiceVariable, *regionChoiceNames)
regionChoiceDropdownMenu.config(width=40, font=('Helvetica', 12))
regionChoiceDropdownMenu.grid(row=1,column=1)

chosenRegions = []
addedRegionsLabel = Label(top, text="", font=('Helvetica', 12), fg='black')
def regionAddCallback(*args):
    if not regionChoiceVariable.get() in chosenRegions:
        chosenRegions.append(regionChoiceVariable.get())
        addedRegionsLabel.configure(text="Added Regions include: {}".format(chosenRegions))
        addedRegionsLabel.pack()
def regionRemoveCallback(*args):
    if regionChoiceVariable.get() in chosenRegions:
        chosenRegions.remove(regionChoiceVariable.get())
        addedRegionsLabel.configure(text="Added Regions include: {}".format(chosenRegions))
        addedRegionsLabel.pack()
regionAddButton = Button(regionFrame, text="Add", fg="green", command=regionAddCallback).grid(row=1,column=2)
regionRemoveButton = Button(regionFrame, text="Remove", fg="red", command=regionRemoveCallback).grid(row=2,column=2)
regionFrame.pack()

regionToEditOptions = []
if len(chosenRegions) == 0:
    regionToEditOptions.append("---")
else:
    regionToEditOptions = chosenRegions

regionEditChoiceVariable = StringVar(top)
regionEditChoiceVariable.set("---")
regionEditChoiceDropdownMenu = OptionMenu(top, regionEditChoiceVariable, *regionToEditOptions)
regionEditChoiceDropdownMenu.config(width=90, font=('Helvetica', 12))
regionEditChoiceDropdownMenu.pack()

def regionDropdownCallback(*args):
    generateDinoMapFrame(top,regionEditChoiceVariable.get())
regionEditChoiceVariable.trace("w", regionDropdownCallback) 

top.mainloop()
