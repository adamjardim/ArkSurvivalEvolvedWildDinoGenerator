from tkinter import *
import dinoCodeGeneratorUtility
from GUIUtility import createMapDropDown
from dinoLoader import dinoList
from mapLoader import mapList

chosenMap = -1
chosenRegion = -1
chosenDino = -1

mapLocked = False

def setupGUI(self, topFrame):
    #load map dropdown
    mapChoiceVar = StringVar('---')
    mapDropdown = createMapDropDown(topFrame, mapChoiceVar, mapList, 90)

    #Get map choice from dropdown
    chosenMap = mapChoiceVar.get()

    #load lockMapButton
    def lockMapCallback(*args):
        if not mapLocked:
            mapLocked = True
            #createRegionDropdown(topFrame)
        else:
            #prompt "Are you sure?" dialog
            if messagebox.askyesno('Map Choice', 'Are you sure you want to change map choice?  This will reset your dino choices.'):
                messagebox.showwarning('Yes', 'Not yet implemented')
            else:
                messagebox.showinfo('No', 'Quit has been cancelled')
    mapLockedButton = Button(topFrame, text="Update Map", fg="green", command=lockMapCallback)

    #regionChoiceDropdown = createRegionDropdown(chosenMap)

    #Get region choice from dropdown
    #chosenRegion = getRegionChoice(regionChoiceDropdown)

    #if region choice is valid, load dinos from dropdown
    #if chosenRegion != someinvalidchoice && chosenMap != someinvalidchoice
    #dinoChoiceDropdown = createDinoDropdown()

    #Get dino choices
    #chosenDino = getDinoChoice(dinoChoiceDropdown)

top = Tk()
top.geometry("1000x1000")
top.title("Ark Dino Code Generator")

introText = Label(top, text="Welcome to the Ark Dino Code Generator.")
introText.pack()

setupGUI(top)

top.mainloop()