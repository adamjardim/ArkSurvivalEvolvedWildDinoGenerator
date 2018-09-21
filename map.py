class arkMap(object):

    listOfRegions = list()

    def __init__(self, name, regionList):
        self.listOfRegions = regionList
        self.name = name

    def getName(self):
        return self.name

    def getListOfRegions(self):
        return self.listOfRegions
