import random

from project.logic.mapHelper import MapHelper
from project.model.sheep import Sheep


class SheepFactory:
    init_pos_limit = 10

    def create_sheep(self, number):
        sheepList = list()
        while len(sheepList) < int(number):
            generatedX = round(random.uniform(0.000, self.init_pos_limit), 3)
            generatedY = round(random.uniform(0.000, self.init_pos_limit), 3)
            if MapHelper.is_coordinate_empty(generatedX, generatedY, sheepList):
                sheepList.append(Sheep(len(sheepList) + 1, generatedX, generatedY))
        return sheepList
