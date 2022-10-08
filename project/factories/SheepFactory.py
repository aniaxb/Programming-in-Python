import random
from project.model.sheep import Sheep

class SheepFactory:

    def __init__(self, init_pos_limit):
        self.init_pos_limit = init_pos_limit

    def createSheep(self, number):
        list = []
        for i in range(number):
            randomCoordinatesX = round(random.uniform(0.000, self.init_pos_limit), 3)
            randomCoordinatesY = round(random.uniform(0.000, self.init_pos_limit), 3)
            list.append(Sheep(i, randomCoordinatesX, randomCoordinatesY))
        for obj in list:
            print(obj.__str__())


