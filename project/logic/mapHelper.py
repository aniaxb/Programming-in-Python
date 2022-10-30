import random
import math

from project.model.sheep import Sheep
from project.model.wolf import Wolf


def is_coordinate_empty(coX: float, coY: float, sheep_list: list, wolf: Wolf):
    if (coX is wolf.coX) and (coY is wolf.coY):
        return False
    for entity in sheep_list:
        if (coX is entity.coX) and (coY is entity.coY) and entity.isAlive:
            return False
    return True


def calculate_distances(sheep_list: list, wolf: Wolf):
    for entity in sheep_list:
        if entity.isAlive:
            entity.distance = round(
                math.sqrt(pow(entity.get_x() - wolf.get_x(), 2) + pow(entity.get_y() - wolf.get_y(), 2)), 3)


def simulate_direction():
    return random.choice("NEWS")


def get_sheep_cords(sheep: Sheep, wolf: Wolf):
    wolf.coX = sheep.coX
    wolf.coY = sheep.coY
