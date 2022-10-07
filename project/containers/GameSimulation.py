from array import array

from project.factories.SheepFactory import SheepFactory


class GameSimulation:
    sheepRepository: array

    def __int__(self, init_pos_limit, sheep_amount, sheep_move_dist, wolf_move_dist):
        self.init_pos_limit = init_pos_limit
        self.sheep_amount = sheep_amount
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        sheepRepository = SheepFactory(init_pos_limit).createSheep(sheep_amount)

    def startSimmulation(self, rounds_number):
        return ""


    def moveSheeps(self):
        return ""
