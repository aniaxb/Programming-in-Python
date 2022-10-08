from project.exceptions.Exceptions import SheepViabilityException
from project.factories.SheepFactory import SheepFactory
from project.model.Wolf import Wolf


class GameSimulation:

    def __init__(self, init_pos_limit, sheep_amount, sheep_move_dist, wolf_move_dist):
        self.init_pos_limit = init_pos_limit
        self.sheep_amount = sheep_amount
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.entityRepository = list()

    def startSimulation(self, rounds_number):
        try:
            self.entityRepository = SheepFactory().createSheep(self.sheep_amount)
            self.entityRepository.append(Wolf(0, 0))

            for i in range(rounds_number):
                self.moveSheeps()
                self.moveWolf()
            return True

        except SheepViabilityException:
            return True
        except Exception:
            return False

    def moveSheeps(self):
        return ""

    def moveWolf(self):
        return ""

    def __str__(self):
        return "GameSimulation Map Status[" + str(self.entityRepository) + "]"
