import logging
import random

from project.exceptions.exceptions import sheep_viability_exception, logic_exception
from project.factories.sheepFactory import SheepFactory
from project.logic.mapHelper import is_coordinate_empty
from project.model.wolf import Wolf
from project.model.sheep import Sheep


def simulate_direction():
    return random.choice("NEWS")


class GameSimulation:

    def __init__(self, init_pos_limit, sheep_amount, sheep_move_dist, wolf_move_dist):
        self.init_pos_limit = init_pos_limit
        self.sheep_amount = sheep_amount
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.entityRepository = list()

    def start_simulation(self, rounds_number):
        self.entityRepository = SheepFactory().create_sheep(self.sheep_amount)
        self.entityRepository.append(Wolf(0, 0))
        try:
            for i in range(rounds_number):
                logging.info("rounds_number:" + str(i + 1) + "\n" + self.__str__())
                self.move_sheeps()
                self.move_wolf()
            return True
        except sheep_viability_exception:
            return False

    def move_sheeps(self):
        for sheep in self.entityRepository:
            if isinstance(sheep, Sheep):
                self.change_coordinates(sheep)

    def move_wolf(self):
        return ""

    def change_coordinates(self, sheep: Sheep):
        if not sheep.isAlive:
            return
        genX = sheep.coX
        genY = sheep.coY
        match simulate_direction():
            case "N":
                genY += self.sheep_move_dist
            case "S":
                genY -= self.sheep_move_dist
            case "W":
                genX -= self.sheep_move_dist
            case "E":
                genX += self.sheep_move_dist
            case _:
                raise logic_exception()
        if is_coordinate_empty(genX, genY, self.entityRepository):
            sheep.coX = genX
            sheep.coY = genY
            return
        else:
            logging.warning("The drawn coordinate is busy")
            self.emergency_move(sheep)

    def emergency_move(self, sheep: Sheep):
        genX = sheep.coX
        genY = sheep.coY
        if is_coordinate_empty(genX, genY + self.sheep_move_dist, self.entityRepository):
            sheep.coY = genY + self.sheep_move_dist
            return
        elif is_coordinate_empty(genX, genY - self.sheep_move_dist, self.entityRepository):
            sheep.coY = genY - self.sheep_move_dist
            return
        elif is_coordinate_empty(genX + self.sheep_move_dist, genY, self.entityRepository):
            sheep.coX = genX + self.sheep_move_dist
            return
        elif is_coordinate_empty(genX - self.sheep_move_dist, genY, self.entityRepository):
            sheep.coX = genX + self.sheep_move_dist
            return
        else:
            logging.warning("Cannot move Sheep!")

    def __str__(self):
        result = ""
        for entity in self.entityRepository:
            result = result + entity.__str__() + "\n"
        return "GameSimulation Map Status[\n" + result + "]"
