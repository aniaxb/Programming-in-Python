import random

from project.logic.MapHelper import MapHelper
from project.model.Sheep import Sheep


class SheepFactory:
    init_pos_limit = 10

    def createSheep(self, number):
        sheepList = list()
        while len(sheepList) < int(number):
            generatedX = round(random.uniform(0.000, self.init_pos_limit), 3)
            generatedY = round(random.uniform(0.000, self.init_pos_limit), 3)
            if MapHelper.isCoordinateFree(generatedX, generatedY, sheepList):
                sheepList.append(Sheep(len(sheepList) + 1, generatedX, generatedY))
        return sheepList
