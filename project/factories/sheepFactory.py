import random

from project.logic.mapHelper import is_coordinate_empty
from project.model.sheep import Sheep


class SheepFactory:
    init_pos_limit = 10

    def create_sheep(self, number):
        sheepList = list()
        while len(sheepList) < int(number):
            generatedX = round(random.uniform(-self.init_pos_limit, self.init_pos_limit), 2)
            generatedY = round(random.uniform(-self.init_pos_limit, self.init_pos_limit), 2)
            if is_coordinate_empty(generatedX, generatedY, sheepList):
                sheepList.append(Sheep(len(sheepList) + 1, generatedX, generatedY))
        return sheepList
