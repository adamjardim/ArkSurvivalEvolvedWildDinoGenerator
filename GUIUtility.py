from tkinter import *
import dinoCodeGeneratorUtility
from dinoLoader import dinoList
from mapLoader import mapList

def createMapDropDown(topFrame, mapChoiceVariable, mapOptions, dropWidth):
    mapChoiceNames = []
    for mapChoice in mapOptions:
        mapChoiceNames.append(mapChoice.getName())
    mapChoiceVariable.set("---")
    mapChoiceDropdownMenu = OptionMenu(topFrame, mapChoiceVariable, *mapChoiceNames)
    mapChoiceDropdownMenu.config(width=dropWidth, font=('Helvetica', 12))
    mapChoiceDropdownMenu.pack()
    return mapChoiceDropdownMenu

def createRegionDropdown(topFrame, regionChoiceVariable, mapToGetRegions, dropWidth):
    regionChoiceVariable.set("---")
    regionChoiceDropdownMenu = OptionMenu(topFrame, regionChoiceVariable, *mapToGetRegions.getListOfRegions())
    regionChoiceDropdownMenu.config(width=dropWidth, font=('Helvetica', 12))
    return regionChoiceDropdownMenu

def createDinoDropdown(topFrame, dinoChoiceVariable, dinoOptions, dropWidth):
    dinoChoiceNames = []
    for dinoChoice in dinoOptions:
        dinoChoiceNames.append(dinoChoice.getName())
    dinoChoiceVariable.set("---")
    dinoChoiceDropdownMenu = OptionMenu(topFrame, dinoChoiceVariable, *dinoChoiceNames)
    dinoChoiceDropdownMenu.config(width=dropWidth, font=('Helvetica', 12))
    return dinoChoiceDropdownMenu