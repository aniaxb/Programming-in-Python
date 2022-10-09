import logging
import unittest

from project.factories.sheepFactory import SheepFactory
from project.logic.gameSimulation import GameSimulation
from project.logic.mapHelper import is_coordinate_empty
from project.model.sheep import Sheep
from project.model.wolf import Wolf


class MyTestCase(unittest.TestCase):
    def test_MapHelper(self):
        repo = GameSimulation(0, 0, 0, 0).entityRepository
        repo.append(Sheep(0, 1, 1))
        repo.append(Sheep(1, 1, 2))

        self.assertEqual(len(repo), 2)
        self.assertEqual(is_coordinate_empty(1, 1, repo), False)
        self.assertEqual(is_coordinate_empty(1, 2, repo), False)
        self.assertEqual(is_coordinate_empty(1, 3, repo), True)

        repo[0].isAlive = False
        self.assertEqual(is_coordinate_empty(1, 1, repo), True)

    def test_Wolf(self):
        wolf = Wolf(0, 1)

        self.assertEqual(wolf.coX, 0)
        self.assertEqual(wolf.coY, 1)
        self.assertEqual(wolf.sheep_counter, 0)

    def test_Sheep(self):
        sheep = Sheep(0, 1, 2)

        self.assertEqual(sheep.id, 0)
        self.assertEqual(sheep.coX, 1)
        self.assertEqual(sheep.coY, 2)
        self.assertTrue(sheep.isAlive)

        sheep.isAlive = False
        self.assertFalse(sheep.isAlive)

    def test_sheep_factory(self):
        factory = SheepFactory().create_sheep(15)
        self.assertEqual(len(factory), 15)

    def test_simulation(self):
        game = GameSimulation(10, 15, 0.5, 1)
        self.assertTrue(game.start_simulation(50))


if __name__ == '__main__':
    unittest.main()
