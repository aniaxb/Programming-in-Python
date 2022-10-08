from project.model.sheep import Sheep
from project.model.wolf import Wolf


class GameSimulation:

    def __init__(self, init_pos_limit, sheep_amount, sheep_move_dist, wolf_move_dist):
        self.init_pos_limit = init_pos_limit
        self.sheep_amount = sheep_amount
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.entityRepository = list()

    def startSimulation(self, rounds_number):
        self.entityRepository.append(Wolf(0, 0))
        self.entityRepository.append(Sheep(1, 2, 3))
        return self.entityRepository

    def moveSheeps(self):
        return ""
