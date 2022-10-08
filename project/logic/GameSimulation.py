import random

from project.exceptions.Exceptions import SheepViabilityException, LogicException
from project.factories.SheepFactory import SheepFactory
from project.logic.MapHelper import MapHelper
from project.model.Wolf import Wolf
from project.model.Sheep import Sheep


def simulateDirectory():
    return random.choice("NEWS")


class GameSimulation:

    def __init__(self, init_pos_limit, sheep_amount, sheep_move_dist, wolf_move_dist):
        self.init_pos_limit = init_pos_limit
        self.sheep_amount = sheep_amount
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.entityRepository = list()

    def startSimulation(self, rounds_number):
        self.entityRepository = SheepFactory().createSheep(self.sheep_amount)
        self.entityRepository.append(Wolf(0, 0))
        try:
            for i in range(rounds_number):
                print("rounds_number:" + str(i) + "\n" + self.__str__())
                self.moveSheeps()
                self.moveWolf()
            return True
        except SheepViabilityException:
            return False

    def moveSheeps(self):
        for sheep in self.entityRepository:
            if isinstance(sheep, Sheep):
                self.changeCoordinates(sheep)
                    #TODO: draw coordinates or switching to emergency state and checking NEWS manually

    def changeCoordinates(self, sheep: Sheep):
        genX = sheep.coX
        genY = sheep.coY
        match simulateDirectory():
            case "N":
                genY += self.sheep_move_dist
            case "S":
                genY -= self.sheep_move_dist
            case "W":
                genX -= self.sheep_move_dist
            case "E":
                genX += self.sheep_move_dist
            case _:
                raise LogicException()
        if MapHelper.isCoordinateFree(genX, genY, self.entityRepository):
            sheep.coX = genX
            sheep.coY = genY
            return True
        return False

    def moveWolf(self):
        return ""

    def __str__(self):
        result = ""
        for entity in self.entityRepository:
            result = result + entity.__str__() + " "
        return "GameSimulation Map Status[" + result + "]"
