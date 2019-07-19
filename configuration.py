from dino import dinosaur
from map import arkMap
from mapLoader import mapList
from dinoLoader import dinoList

class configuration(object):

    listOfRegionConfigs = []

    def __init__(self, map):
        self.map = map
    def addRegion(self, regConfig):
        self.listOfRegionConfigs.append(regConfig)
        print("Region Added: ", regConfig.name)
    def addRegions(self, regConfigs):
        for regConfig in regConfigs:
            self.addRegion(regConfig)
    def printConfig(self):
        print("Configuration:")
        print("Map: ", self.map.name)
        for region in self.listOfRegionConfigs:
            print("\tRegion: ", region.name)
            print("\t\tW/M: ", region.weight, "/", region.max)
            print("\t\tDinos (", len(region.dinosInRegion),") : ")
            for dino in region.dinosInRegion:
                print("\t\t\t- ", dino.name)

class regionConfiguration(object):
    dinosInRegion = []

    def __init__(self, name):
        self.name = name
        print("\tNew Region: ", self.name)

    def setEntryWeight(self, weight):
        self.weight = weight
        print("\t\tSet Weight: ", self.weight)

    def setMax(self, max):
        self.max = max
        print("\t\tSet Max: ", self.max)

    def addDino(self, dinoNum):
        self.dinosInRegion.append(dinoList[dinoNum])
        print("\t\t\tAdded dino: ", dinoList[dinoNum].name)

    def addDinos(self, dinoList):
        for dinoNum in dinoList:
            self.dinosInRegion.append(dinoList[dinoNum])
            print("Added dino: ", dinoList[dinoNum].name)

    def resetDinos(self):
        self.dinosInRegion.clear()