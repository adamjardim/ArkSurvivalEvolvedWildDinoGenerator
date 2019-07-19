from dino import dinosaur
from map import arkMap
from mapLoader import mapList
from dinoLoader import dinoList

class configuration(object):

    listOfRegionConfigs = list()

    def __init__(self, map, regionList):
        self.listOfRegions = regionList
        self.map = map
    def addRegion(self, regConfig)

class regionConfiguration(object):
    dinosInRegion = list()

    def __init__(self, name):
        self.name = name

    def addDino(self, dinoNum):
        dinosInRegion.append(dinoList[dinoNum])



    